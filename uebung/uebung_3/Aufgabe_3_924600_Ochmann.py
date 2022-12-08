"""
    Aufgabe_03.py
"""


def remove_strings(text, string_list):
    for char in string_list:
           
       text_cleaned = text.replace(char, "")
    


    return text_cleaned
"""
Leider hänge ich bei dieser Lösung, 
ich gehe davon aus das die Aufgabe genau dieses Problem als Challange hat, 
aber ich habe keine Ahnung warum es nicht funktioniert, obwohl es sollte.  
"""

"""
    Besipiel Ausgabe
"""

text_cleaned = remove_strings("ja, nein, vielleicht",["ja", "nein", ","])
                                
print(text_cleaned) # => vielleicht


#text_cleaned = remove_strings("Dann sagte ich: 'Ja, das geht.'", ["\'",".", ",", ":"])
                                
#print(text_cleaned) # => Dann sagte ich Ja das geht
