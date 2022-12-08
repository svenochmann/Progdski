"""
    Aufgabe 4
"""
import time
import sys
def done():
    print("Herzlichenglückwunch!!!")
    print("Du bist raus gekommen.")
    reload=input("Nochmal Spielen(Yes) oder abrechen(No)")
    if reload.lower() =="yes":
        start()
    else:
         sys.exit("Spiel wird Beendet")
         


            
def tot():
    print("Du bist gestorben!!!!")
    reload=input("Nochmal Spielen(Yes) oder abrechen(No)")
    if reload.lower() =="yes":
        start()
    else:
         sys.exit("Spiel wird Beendet")
        

#Funktion warted 3 sek
def warten():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Genug gewarted!!")
    
    
#Funktion ruft ohne das was passiert
def rufen():
    print("HALLO!!")
    time.sleep(2)
    print("nichts passiert")
    
    
def start():
    
    print("Du befindest dich in einem unbekannten, dunklen Raum...")
    raum_1("")
        

def raum_1(modus):
    def lichtschalter():
        print("Die Wände fühlen sind an wie aus Fels.")
        time.sleep(2)
        print("Nirgendwo ein Schalter!")
        time.sleep(2)
        print("Doch halt! Da ragt etwas aus der Wand heraus... ein metallischer Hebel.")
        action=input("a) Ich betätige den Hebel b) Ich suche lieber noch weiter: ")
        if action.lower() == "a":
            raum_1("licht")
        else:
            time.sleep(1)
            print("Hier scheint nichts zu sein")
            raum_1("")
    
    if modus =="":    
        action=input("Was machst du? a) Rufen b) Lichtschalter suchen c) Warten: ")
        if action.lower() ==  "a":
            rufen()
        elif action.lower()  == "b":
            lichtschalter()
        elif action.lower() == "c":
            warten()
            raum_1("")
        else:
            print("Invalid")  
    elif modus =="licht":
        print("Du Stauns.")
        
        time.sleep(2)
        print("Du befindest dich in einer Höhele")
        time.sleep(2)
        print("An der Decke ist eine Mahlere die folgendes Abildet:")
        print("Eine Katze , einen Hund und ein Huhn")
        time.sleep(2)
        print("Erst danch felt dir auf das vor dir 2 Türen sind")
        action=input("Öffne: a) Die Linke Tür oder b) Die Rechte Tür :")
        if action.lower() == "a":
           print("Aus der gerade geöffneten Tür.")
           print("springt eine Genetisch veränderte Katze.")
           
           tot()
        else:
            raum_2pre()

         
def raum_2pre():        
      print("Du findest dich in einem dir unbekanten labor wieder.")
      time.sleep(2)
      print("Es sieht verlassen auf")
      time.sleep(2)
      print("Auf der gegenüberliegende seite sist du eine Tür mit einem grün")
      print("leuchtendem Exit schild")
      time.sleep(2)
      raum_2()          
            
    
    
def raum_2():
    def raetsel(wert_1,wert_2,wert_3):
        if wert_1.lower() =="katze" and wert_2.lower() == "hund" and wert_3.lower() =="huhn":
            raum_3pre()
        else:
            print("falsch")
            print("tipp: Raum 1")
            tuer()            
        
    def tuer():
        print("Die Tür hat ein Schloss")
        time.sleep(2)
        print("Gebe folgende begriffe in die rihtige reihen folge:")
        print("Hund, Katze, Huhn")
        wert_1=input("Gebe den ersten begriff an: ")
        wert_2=input("Gebe den zweiten begriff an: ")
        wert_3=input("Gebe den dritten begriff an: ")
        raetsel(wert_1,wert_2,wert_3)         
        
        
    action=input("a) zur Tür gehen oder b) noch umsehen:")
    if action.lower() == "b":
        time.sleep(1)
        print("Hier sind nur verstaubte geräte")
        time.sleep(1)
        print("und kapute gehäge")
        raum_2()
    elif action.lower() == "a":
        tuer()
    else:
        print("invalid")
        raum_2()
        
    return None


def raum_3pre():
    print("Die Tür öffnet sich!!!!")
    time.sleep(2)
    print("Du leufst raus.")
    time.sleep(2)
    print("Du artmest die Frische luft ein")
    time.sleep(2)
    print("Vor dir sind drei pfade was tust du")
    raum_3()


    
def raum_3():
    def pfad_1():
        time.sleep(3)    
        print("du bist wieder am labor ausgang.")
        raum_3()
        return None
    
    action=input("a)Pfad 1 nehmen b) Pfad 2 nehmen c)Pfad 3 nehmen")
    if action.lower() == "a":
        print("Du nimmst den ersten pfad")
        
        pfad_1()
    elif action.lower() =="b":
        print("Du findest ein Dorf und bist gereted")
        done()
    elif action.lower() =="c":
        print("du verläust dich")
        tot()
    else:
        print("invalid")
        raum_3()
        

        



start()
raum_1("")

