"""
    Aufgabe 2
"""



credit= 1000.00
delta=0.99
#um zu zählen wie oft ich etwas abziehen konnte [punkt 3]
count=0
while True:
    if credit- delta > 0: 
        
        credit = credit - delta
        count = count +1
        print(credit)
    else:
        
        break

"""
Wenn wir mit credit = 1000 und delta = 0.9999 starten, welchen Wert hat credit 
nach beenden der while-Schleife?

Antwort:
        0.09999999999228715
"""
"""
Bei welcher Art von Werten für credit und delta bekommen wir Probleme mit der
Ausführung des Programmes? (und: Warum?)

Antwort:
        -Es kommt zu Errors wenn man keinen Int/float eingibt sonder 
         liste, string, etc.. eingibt
        -
        
"""
    
    
"""
Wie könnten wir die while-Schleife ergänzen, so dass wir zum Schluss 
auch ausgeben können wie oft delta von credit entnommen wurde?

Antwort:
        indem wir ihn bei jedem loop mit zählen lassen mit hilfe einer variable.
"""    
