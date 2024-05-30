## deriving the new class from old class 
## inherite the properties of old class in new class 
## If a class  is dervied from one base class (parent class) its called single inheritance

class Father:
    money=1000

    def show(self):
        print("Parent Class Instance method")

    @classmethod
    def showmoney(cls):
        print("parent class method:",cls.money)

    @staticmethod
    def stat():
        a=10
        print("static method called :", a)



class Son(Father):
    def disp(self):
        print("child class instance method")
# child class obj
s=Son()
s.disp()

s.show()
s.stat()





