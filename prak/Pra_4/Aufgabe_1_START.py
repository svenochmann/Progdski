import numpy as np


def get_numpy_array_infos(array):
    
    print(array.dtype)
    print(array.size)
    print(array.shape)
    print(np.min(array))
    print(np.max(array))
    
    pass

def min_max_scaling(array):
    norm_arr = (array-np.min(array)) / (np.max(array)-np.min(array))

    
    
    return norm_arr


"""Creating Array"""
arr=np.arange(1,128,2).reshape((8,8))




"""Ausgabe"""
#get_numpy_array_infos(arr)
norm_arr = min_max_scaling(arr)
get_numpy_array_infos(arr)
get_numpy_array_infos(norm_arr)



























