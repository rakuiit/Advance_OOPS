## many forms
## if a variable ,object and method show different behavior according to situation  its called polymorphism

class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
    
class Horse:
    def walk(self):
        print("tandak tandak tandak tandak")


def myfunction(obj):
    obj.walk()

d=Duck()
myfunction(d)
