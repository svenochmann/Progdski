"""
    Aufgabe 1
"""


"""
    Aufgabe 1.1
"""
"""
list_1 = [50, 40, 30, 100]

list_2 = [10, 20, 1, 51]

list_3 = list_1 +list_2
list_3.sort()
"""

"""
    Aufgabe 1.2
"""

def list_combiner(list_1, list_2):
    combined_list= list_1 + list_2
    combined_list.sort()
    
    return combined_list

"""
    Beispiel
"""
combined_list = list_combiner([1, 2, 3], [2.5, 0.5, 1.5])
print(combined_list) # -> soll ausgeben: [0.5, 1, 1.5, 2, 2.5, 3]

