import numpy as np
size = 2

x = np.zeros((size-2,size-2))
x = np.pad(x, pad_width=1, mode='constant', constant_values=1)
print(x)