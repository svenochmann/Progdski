"""Aufgabe 2"""

class Person:
    def __init__(self, name, mail, password):
            self.__name = name
            self.__mail = mail
            self.__check_password(password)
            self.__password = password
            self.__failed_attempts = 0

    def __check_password(self, password):
        assert len(password) >= 8, \
            "Password must have at least 8 characters"

    def get_name(self):
        return self.__name

    def get_mail(self, password):
        if self.__failed_attempts < 3:
            if self.__password != password:
                self.__failed_attempts += 1
                print("Password incorrect.")
            elif self.__password == password:
                print(self.__mail)
                self.__failed_attempts = 0
            else:
                print("invalid")
        
        else:
            print("Too many failed attempts.")
        return



"""Beispiel Ausgabe"""
"""
p1=Person("Monica", "m.thomson@gmail.com", "SuperSecret")

p1.get_mail("FirstGuess")  # => Password incorrect.
p1.get_mail("SecondGuess")  # => Password incorrect.
p1.get_mail("ThirdGuess")  # => Password incorrect.
p1.get_mail("ThirdGuess")  # => Password incorrect.
"""
p1=Person("Monica", "m.thomson@gmail.com", "SuperSecret")

p1.get_mail("FirstGuess")   # => Password incorrect.
p1.get_mail("SecondGuess")  # => Password incorrect.
p1.get_mail("SuperSecret")  # => m.thomson@gmail.com
p1.get_mail("FirstGuess")   # => Password incorrect.
p1.get_mail("SecondGuess")  # => Password incorrect.
p1.get_mail("ThirdGuess")   # => Password incorrect.
p1.get_mail("SuperSecret")  # => Too many failed attempts.