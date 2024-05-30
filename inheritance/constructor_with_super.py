## how we can call parent class constructor when we have constructor in both the class 
## super method  is used to call parent class constructor or method from child class 


class Father:
    def __init__(self):
        print("parent class constructor")
    def show(self):
        print("parent class isntance method")



class Son(Father):
    def __init__(self):
        super().__init__()   # calling parent call constructor 
        print("child class constructor")
    def disp(self):
        print("child class isntance method")

s=Son()


