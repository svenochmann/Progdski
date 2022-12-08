"""
#region Aufgabe 1 //Bonus
def hackerize(text):
    for letter in text:
        if letter.lower() =="e":
            text = text.replace("e", "3")
        elif letter == "i":
            text = text.replace("i", "!")
        elif letter == "o":
            text = text.replace("o", "0")
        elif letter == "s":
            text = text.replace("s", "5")
        else:
            pass
              
        
    return text  




print(hackerize("I write my text like passwords")) 
# --> I wr!t3 my t3xt l!k3 pa55w0rd5
#endregion
"""


#region Aufgabe 2 / 2.1
def read_text_file(filename):
    newfile = open(f"{filename}", "r")
    data = newfile.read()
    return str(data)

def text_to_words(text):
    split_text = text.split()
    return split_text

#region 2.1
#Text file wird gelesen
test= read_text_file("/home/sven/git/ProgDSKI-Praktikum/Pra_2/de_la_mettrie_mensch_maschine_UTF8.txt")

#Wie viele Wörter
#sind im Buch "Der Mensch eine Maschine" insgesamt enthalten?
wordcount = len(text_to_words(test))
print(wordcount)
#Wie viele verschiedene Wörter sind in diesem Buch enthalten?
uniquewords = len(set(text_to_words(test)))
print(uniquewords)
#endregion

#region 2.2
def word_counter(text):
    words = text_to_words(text)
    words = list(words)
    dict_words =dict()
    dict_words = dict.fromkeys(words, 0)
    for word in words:
        if word in dict_words:
            dict_words[word] = dict_words.get(word, 0) + 1
        else:
            pass            

    return dict_words

dict_text = word_counter(test)
"""
#Wie oft kommen die folgenden Wörter im Text vor:
#"Mensch", "Maschine", "das", "Das" 
for key,value in dict_text.items():
    if key =="Mensch":
        print(key,":",value)
    elif key =="Maschine":
        print(key,":",value)
    elif key =="das":
        print(key,":",value)
    elif key =="Das":
        print(key,":",value)
    else:
        pass
"""
#2.3
#Was sind die 10 häufigsten Wörter im Text?
sorted_dict = dict(sorted(dict_text.items(), key=lambda x: -x[1]))
for i in range(10):
    print(list(sorted_dict.items())[i])
    

#endregion



#endregion

