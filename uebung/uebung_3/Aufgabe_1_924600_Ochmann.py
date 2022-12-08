"""
    Aufgabe_01.py
"""

"""Gegebene Variable"""

german_english_pairs = [("Name", "name"), ("Hochschule", "college"), ("Hörsaal",
"lecture hall")]


"""German to English"""
#Given list of tuple into dictonary
ger_eng = dict()
for ger,eng in german_english_pairs:
    ger_eng.setdefault(ger, []).append(eng)



"""English to German"""
#Given list of tuple into dictonary but reverse
eng_ger =dict()
for ger,eng in german_english_pairs:
    eng_ger.setdefault(eng, []).append(ger)



"""Beispiel Ausgabe"""



print(ger_eng["Hörsaal"]) # --> lecture hall
print(eng_ger["college"]) # --> Hochschule