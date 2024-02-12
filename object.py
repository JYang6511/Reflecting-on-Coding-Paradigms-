# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"




podracer1 = AnakinsPod(1000, "used", 5000)
podracer2 = SebulbasPod(800, "damaged", 3000)

# Test repair method
print("Before repair:", podracer1.condition)
podracer1.repair()
print("After repair:", podracer1.condition)

# Test boost method
print("Before boost:", podracer1.max_speed)
podracer1.boost()
print("After boost:", podracer1.max_speed)

# Test flame_jet method
print("Before flame jet:", podracer2.condition)
podracer2.flame_jet(podracer1)
print("After flame jet:", podracer1.condition)

'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation:

Each class (Podracer, AnakinsPod, SebulbasPod) encapsulates its own data (attributes) and behavior (methods). This encapsulation helps in organizing and managing related functionality within each class.
Inheritance:

Both AnakinsPod and SebulbasPod classes inherit from the Podracer class. This inheritance allows them to inherit attributes and methods from the Podracer class, promoting code reuse and reducing redundancy.
Polymorphism:

polymorphism allows objects of different classes to be treated as objects of a common superclass. 

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

I dont think so.  OOP makes it easy with inheritance and encapsulation

How in particular did Object Oriented Programming assist in the solving of this problem?

Facilitating the organization of related data and behavior into coherent units (classes).
Providing a clear structure of different types of podracer objects with common characteristics (Podracer) while allowing for specialization through inheritance.

'''