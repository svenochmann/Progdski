import numpy as np

def keep_cross(arr, n_row,n_col):
    new_arr = np.zeros((4,4))
    for i in range(4):
        new_arr[i,n_row-1] = arr[i,n_row-1]
    
    for i in range(4):
        new_arr[n_col-1,i] = arr[n_col-1,i]
    
     
    return new_arr




my_arr=np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])


print(keep_cross(my_arr, 2, 3))