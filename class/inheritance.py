class Mamalia:
  def walk(self):
    print("walk")
    
    
class Dog(Mamalia):
  def bark(self):
    print("Bark")
    
    
class Cat(Mamalia):
  def be_annoying(self):
    print("Annoying")
    
    
dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.be_annoying()