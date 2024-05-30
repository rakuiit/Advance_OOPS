## many forms
## if a variable ,object and method show different behavior according to situation  its called polymorphism

class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
    
class Horse:
    def walk(self):
        print("tandak tandak tandak tandak")

class Cat:
    def talk(self):
        print("Meow Meow")


def myfunction(obj):
    ## strong typing
    if hasattr(obj,'walk'):
        obj.walk()

d=Duck()
myfunction(d)

