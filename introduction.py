class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name}. I'm {self.age} years old and I'm from {self.country}.")

person1 = Person("Ivan", 19, "Mexico")

person2 = Person("Jeffrey", 32, "Russia")

person1.introduce_yourself()
person2.introduce_yourself()
