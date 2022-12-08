import numpy as np

def create_square(size):
    assert size >=2, "size must be >=2"  
    #Creating a array with zeros
    arr = np.zeros((size-2, size-2))
    #on top of all zeros comes a 1
    arr = np.pad(arr, pad_width=1, mode='constant', constant_values=1)
    return arr 

a=create_square(2)
print(a)
# soll ergeben:
# [[ 1.1. ]
#  [ 1.1. ]]


a=create_square(5)
print(a)
# # soll ergeben:
# [[ 1.1.1.1.1.]
#  [ 1.0.0.0.1.]
#  [ 1.0.0.0.1.] 
#  [ 1.0.0.0.1.]
#  [ 1.1.1.1.1.]]

"""
Glaube nicht das die richtige lösung ist aber es geht
"""