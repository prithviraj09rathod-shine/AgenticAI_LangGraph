class Person:
 def __init__(myself, name, age):
        myself.name = name
        myself.age = age  

 def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  

 def myfun(etc):
    print("This is a sample function without using self.")

# Example usage
person1 = Person("Shine", 30)       
person1.greet()
person1.age = 31  # Update age
person1.greet() 
person2 = Person("Reshma", 25)
person2.greet()
p3 = Person("Anu", 28)
p3.greet()
person1.myfun() 
p3.myfun()


'''polymorphism example-
many forms of a single function. In this example, the move() function behaves 
differently based on the object calling it.'''
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


'''Inheritance example-
 deriving/inheriting properties from a parent class.Here Vehicle is the parent class
 and Car, Boat, Plane are the child classes'''
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

