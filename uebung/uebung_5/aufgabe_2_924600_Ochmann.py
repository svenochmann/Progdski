""""Aufgabe 2"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(person1, person2):
        if person1.age == person2.age:
            print(f"{person2.name} is younger than me.")
        elif person1.age > person2.age:
            print(f"{person2.name} is the same age.")
        else:
            print(f"{person2.name} is older than me.")




person1 = Person("Sally", 77)
person2 = Person("Henry", 77)
person3 = Person("Pieter", 17)


person1.compare_age(person2) # => "Henry is the same age."
person1.compare_age(person3)  # => "Pieter is younger than me."
person3.compare_age(person1)  # => "Sally is older than me."



