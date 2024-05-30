# by default constructor in parent class  is availble to the child class 


class Father:
    def __init__(self):
        self.money=1000
        print("Father class Constructor")
    
    def show(self):
        print("Father class Instance Method")


class Son(Father):
    def disp(self):
        print("son class instance method")


s=Son()
print(s.money)


        