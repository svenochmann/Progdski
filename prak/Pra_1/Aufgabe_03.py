"""
    Aufgabe 3
"""


credit = 1000
debit=[1.1, 22.22, 333.333]
for n in debit:
    if credit >=0:
        credit= credit - n     
    
    else:
        print("credit ist unter null")
    
print(credit)

"""
Wenn wir mit credit = 1000 und debits = [1.1, 22.22, 333.333] starten, welchen
Wert hat credit nach beenden der for-Schleife?

Antwort:
        643.347
"""


"""
Wie können wir den Code verändern,
so dass der Wert credit niemals kleiner Null wird?

Antwort:
        if verzweigung die checkt ob credit noch über null ist.
"""


