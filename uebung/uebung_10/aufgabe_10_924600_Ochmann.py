"""Imports"""
from matplotlib import pyplot as plt
import numpy as np




"""functions"""
def function(x,power1, power2):
    return x**power1 - x**power2




def multi_plot(power1 : list, power2 : list):


    x_values = np.linspace(0,1,100)
    i_count=0
    o_count=1
    #My Code
    for _ in power1:
        for i in range(len(power1)):
            y=function(x_values, power1[i_count], power2[i])
            plt.subplot(4,4,o_count)
            plt.plot(x_values,y)
            o_count+=1
        i_count+=1
        




    plt.show()
    return 

"""Main"""

multi_plot([0.2,2,6,20], [0.1,1,4,10])

































