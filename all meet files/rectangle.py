class Person():
    def __init__(self, name,age,gender,food):
        self.name = name
        self.age = age
        self.gender = gender
        self.food = food
    def Breakfast(self):
        return self.food

person1 = Person("someone", 15, "Straight", "milk")

print(person1.Breakfast())
