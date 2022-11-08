class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(person1, person2):
        if person1 == person2:
            print(f"{person2} is the same age.")
        elif person1 >> person2:
            print(f"{person2}is younger than me.")
        else:
            print(f"{person2} is older than me.")




person1 = Person("Sally", 77)
person2 = Person("Henry", 77)
person3 = Person("Pieter", 17)




person1.compare_age(person2) # => "Henry is the same age."
person1.compare_age(person3)  # => "Pieter is younger than me."
person3.compare_age(person1)  # => "Sally is older than me."




