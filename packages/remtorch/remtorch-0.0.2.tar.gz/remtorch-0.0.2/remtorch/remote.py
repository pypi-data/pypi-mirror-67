from multiprocessing import Process, Event, Manager, Value, Lock
import paramiko
import os
import io
import torch


class RemoteDataset(torch.utils.data.Dataset):
    def __init__(
        self, server, user, password, folder_path, batch_size, shuffle=False, port=22
    ):
        self.server = server
        self.user = user
        self.password = password
        self.port = port
        self.path = folder_path
        self.batch_size = batch_size
        self.shuffle = shuffle

        self.last_index = 0
        self.used_items = 0

        self.manager = Manager()
        self.list = self.manager.list()
        self.count_files = Value("i", 0)
        self.contains_batches = Value("i", 0)

        self.start_load_event = Event()
        self.end_load_event = Event()
        self.is_ready = Event()
        self.locker = Lock()
        self.proc = Process(
            target=self.load, args=(self.start_load_event, self.end_load_event)
        )
        self.proc.daemon = True
        self.proc.start()
        self.is_ready.wait()

    def tick(self, loaded: int, total: int):
        if loaded == total:
            self._storage.seek(0)
            prepared = self.prepare_item(self._storage.read())
            self.list.append(prepared)

    def prepare_item(self, item):
        return NotImplemented

    def load(self, start_event, end_event):
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.server, self.port, self.user, self.password)
        self.transport = self.ssh.get_transport()
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

        self._files = self.sftp.listdir(self.path)
        self.count_files.value += len(self._files)
        self.is_ready.set()

        while True:
            self.locker.acquire()
            start_event.wait()
            for filename in self._files[
                self.last_index : self.last_index + self.batch_size
            ]:
                self._storage = io.BytesIO()
                self.sftp.getfo(
                    os.path.join(self.path, filename), self._storage, callback=self.tick
                )
            self.last_index = (self.last_index + self.batch_size) % self.count_files.value
            self.contains_batches.value += 1
            start_event.clear()
            self.end_load_event.set()
            self.locker.release()

    def __len__(self):
        return self.count_files.value

    def __getitem__(self, idx):
        if self.used_items != 0 and self.used_items % self.batch_size == 0:
            self.contains_batches.value -= 1
            self.used_items = 0
            # we can't use slices because they creating a new object
            # so slices will break multiprocessing compatibility
            for _ in range(self.batch_size):
                del self.list[0]



        if self.contains_batches.value < 2:
            self.start_load_event.set()
            if self.contains_batches.value < 1:
                self.end_load_event.wait()
                self.end_load_event.clear()

        self.used_items += 1
        return self.list[self.used_items - 1]
