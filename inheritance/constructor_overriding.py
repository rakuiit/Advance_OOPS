# what will happen if we define constructor in both the class 
# then parent class constructor is not available for child class 
# child class override behavior of parent class constructor


class Father:
    def __init__(self):
        self.money=1000
        print("Father class Constructor")
    
    def show(self):
        print("Father class Instance Method")


class Son(Father):
    def disp(self):
        print("son class instance method")

    def __init__(self):
        self.money=500
        print("child class Constructor")


s=Son()
print(s.money)



