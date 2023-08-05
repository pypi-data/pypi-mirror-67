===================================
Dataset class to access remote data
===================================

**Example of usage**

.. code-block:: python

    import io
    from PIL import Image
    import numpy as np
    import torch
    from remtorch import RemoteDataset


    class ImageDataset(RemoteDataset):
        def prepare_item(self, item):
          buf = io.BytesIO(item)
          buf.seek(0)
          img = Image.open(buf)
          return np.array(img)

    ds = ImageDataset(
      'servername',
      'username',
      'password',
      '/path/to/files',
      batchsize
    )

    dl = torch.utils.data.DataLoader(ds, batchsize)
    for img in dl:
      # do smth