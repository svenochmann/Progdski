"""Imports"""
import numpy as np
"""Aufgabe 1"""
array_as_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_first_numpy_array = np.array(array_as_list)

"""Aufgabe 1.1"""
#Matrix 8x8
arr_ones = np.ones((5,5))

arr_eye=np.eye(8,dtype=int)

arr_full=np.full((8,8),6,dtype=int)
"""
print(arr_eye)
print(arr_ones)
print(arr_full)
"""



"""Aufgabe 1.2"""
#Other file

"""Aufgabe 1.3"""
#Other file

"""Aufgabe 1.4"""
#print(my_first_numpy_array)
#den Mittelwert aller Koeffizienten 
avg_arr = np.mean(my_first_numpy_array)
#die Mittelwerte der Zeilenelemente
row_arr = np.mean(my_first_numpy_array,axis=0)
#die Mittelwerte der Spaltenelemente
col_arr = np.mean(my_first_numpy_array,axis=1)

print(avg_arr)
print(row_arr)
print(col_arr)
