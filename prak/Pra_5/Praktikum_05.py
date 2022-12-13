#!/usr/bin/env python
# coding: utf-8

# # Praktikum 05 - Jupyter Notebooks und Pandas
# ## Einstieg
# 
# ### Führen Sie die folgenden Code-Blöcke nacheinander aus 

# In[ ]:


my_list = [4, 7, 6, 12, 1]


# In[ ]:


my_list.append(11)


# In[ ]:


my_list.sort()


# In[ ]:


print(my_list)  # my_list


# ### Ergänzen Sie weitere Code-Blöcke und führen Sie beliebige Operationen mit `my_list` aus

# In[ ]:





# ## Pandas

# Das zentrale Element von Pandas heißt **DataFrame**. In diesem Praktikum werden wir mit zwei Datensätzen in Form von .csv-Dateien arbeiten. Diese können von Pandas eingelesen und direkt in einem DataFrame-Objekt gespeichert werden. Vorab werden keine Informationen über die Datensätze preisgegeben. Sie werden die Datensätze untersuchen.

# ### Netflix Datensatz

# In[ ]:


import pandas as pd
import numpy as np
import os


# In[ ]:


root = os.getcwd()
filename = os.path.join(root, "NetflixOriginals.csv")  # je nach eigenem Pfad anpassen!
data = pd.read_csv(filename, sep=",", encoding="ANSI")


# `data`ist nun ein DataFrame-Objekt, welches wir untersuchen können
# 
# #### 1. Überblick verschaffen
# 
# Nutzen Sie folgende Funktionen, um Informationen zum Datensatz zu erhalten.
# - `data.head()`
# - `data.shape`
# - `data.info()`
# - `data.describe()`
# 
# 1. Wie viele Filme sind im Datenset?
# 2. Welche Spalten gibt es und was finden wir darin?
# 3. Wieviele numerische Spalten gibt es?
# 4. Welche durchschnittliche Laufzeit haben die Filme?
# 5. Was ist der höchste IMDB-Score aus dem Datensatz?

# In[ ]:


print(data.head())
print(data.shape())
print(data.info())
print(data.describe())


# #### 2. Weitere Untersuchungen
# 1. Lassen Sie sich alle *unterschiedlichen* Genres aus dem Datensatz ausgeben 
# 2. Wieviele unterschiedliche Genres sind im Datensatz gelistet?
# 3. Welche 20 Genres treten am häufigsten auf?
# 4. Geben Sie die Top20 durch Indexierung an
# 5. Sortieren Sie die Daten von langer zu kurzer Laufzeit der Filme
# 6. Geben Sie nur die Filme aus, dessen Laufzeit länger als 150 ist
# 

# In[ ]:





# ### Pokemon Datensatz

# In[ ]:


import pandas as pd
import numpy as np
import os


# In[ ]:


root = os.getcwd()
filename = os.path.join(root, "pokemon.csv")  # je nach eigenem Pfad anpassen!
data = pd.read_csv(filename, sep=",", encoding="utf-8")
# UTF-8 notwendig um die Japanischen Namen zu lesen, Ansonsten klappt auch ANSI


# In diesem Teil untersuchen wir nur einen Teil des Datensatzes. Dafür treffen wir vorab eine Auswahl an Spalten. Wenn wir die Strings unserer Spaltenwahl in einer Liste speichern und den ursprünglichen Datensatz damit indexieren, erhalten wir ein neues spezifiziertes DataFrame. Bitte ändern Sie die vorgegebene Auswahl nicht.

# In[ ]:


cols = ['name', 'type1', 'type2', 'speed', 'abilities','attack',
           'defense', 'height_m', 'hp', 'weight_kg',
           'generation', 'is_legendary']
data_selected = data[cols]


# #### 1. Überblick verschaffen
# 
# Nutzen Sie folgende Funktionen, um Informationen zum Datensatz zu erhalten.
# - `data_selected.head()`
# - `data_selected.shape`
# - `data_selected.info()`
# - `data_selected.describe()`
# 
# Alle Fragen sind auf `data_selected` zu beziehen:
# 
# 1. Wie viele Pokemon sind im Datenset?
# 2. Welche Spalten gibt es und was finden wir darin?
# 3. Wieviele numerische Spalten gibt es?
# 4. Wie hoch ist die durchschnittliche Angriffspunktzahl aller Pokemon?
# 5. Was ist der höchste Verteidigungswert im Datensatz?
# 6. Gibt es fehlende Einträge im Datensatz?

# In[ ]:





# #### 2. Weitere Untersuchungen
# 1. Schauen Sie sich die fünfte bis zur neunten Zeile der Daten an. Was könnte problematisch sein?
# 2. Ersetzen Sie die problematischen Einträge durch den String "unkown" und schauen Sie sich die Daten nochmal an.
# 3. Wieviele Pokemon gibt es in der ersten Generation?
# 4. Lassen Sie sich die unterschiedlichen `type1`-Typen der Pokemon ausgeben
# 5. Wieviele Pokemon gibt es in den unterschiedlichen `type1`-Typen?
# 6. Erstellen Sie zwei DataFrames `bug_only`und `grass_only`und geben Sie die jeweiligen Mittelwerte für die Angriffsstärke an.
# 7. Lassen Sie sich alle Mittelwerte in Bezug auf `type1` durch Nutzung der `groupby`-Methode ausgeben. In welchem Zusammenhang steht diese Vorgehensweise zur vorherigen Aufgabe?

# In[ ]:




