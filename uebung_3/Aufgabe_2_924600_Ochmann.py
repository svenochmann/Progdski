"""
    Aufgabe_02.py
"""

import random

amount_input =input("Wie häufig wollen Sie würfeln:") 
diced_dict = {1:0,2:0,3:0,4:0,5:0,6:0}
for n  in range(int(amount_input)):
    diced=random.randint(1, 6)    
    if diced == 1:
        diced_dict[1]+=1
    elif diced== 2:
        diced_dict[2]+=1
    elif diced== 3 : 
        diced_dict[3]+=1
    elif diced==4:
        diced_dict[4]+=1
    elif diced==5:
        diced_dict[5]+=1
    elif diced==6:
        diced_dict[6]+=1
    else:
        print("Invalid")
"""
    Beispiel Ausgabe
"""
print(diced_dict)
#{1: 175, 2: 155, 3: 175, 4: 159, 5: 170, 6: 166}
