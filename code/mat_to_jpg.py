import h5py
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

for file in glob.glob('data/*.mat'):
    with h5py.File(file, 'r') as f:
            fname = os.path.basename(f.filename).split('.')[0]
            img = f['cjdata']['image']
            img = np.array(img, dtype=np.float32)
            plt.imsave("images/{}.jpg".format(fname), img, cmap='gray')