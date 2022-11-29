import numpy as np
import random as r


def random129(n_row, n_col):
    final_arr=np.zeros((n_row, n_col), dtype =int)
    numbers = [1,9,2]
    for x in range(n_row):
        for y in range(n_col):
            i=r.randint(0, 2)
            final_arr[x,y-1] = numbers[i]
    return final_arr








print(random129(3, 7))
