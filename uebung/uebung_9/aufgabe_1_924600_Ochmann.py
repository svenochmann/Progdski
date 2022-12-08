"""Aufgabe 1"""

"""Imports"""
import pandas as pd
"""Imports Data"""
data = pd.read_csv("pokemon.csv")

"""Code!"""
weight_low_pok=data['weight_kg'].quantile(.1, interpolation='higher')
weight_high_pok=data['weight_kg'].quantile(.9,interpolation='lower')
slowest_pok=data['speed'].quantile(.1,interpolation='higher')
fastest_pok=data['speed'].quantile(.9,interpolation='lower')

"""Ausgabe"""
#A > Wie schwer maximal sind die leichtesten 10% aller Pokemon?
print(f"10% der leichtesten Pokemon sind Maximal: {weight_low_pok}Kg Schwer.")
#B > Wie schwer minimal sind die schwersten 10% aller Pokemon?
print(f"B) 10% der schwersten Pokemon sind Mindestens: {weight_high_pok}Kg Schwer.")
#C > Wie schnell maximal sind die langsamsten 10% aller Pokemon?
print(f"C) 10% der langsamsten Pokemon sind Maximal: {slowest_pok} Schnell.")
#D > Wie schnell minimal sind die schnellsten 10% aller Pokemon?
print(f"D) 10% der schnellsten Pokemon sind mindestens: {fastest_pok} Schnell.")






























