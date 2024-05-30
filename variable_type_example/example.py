# there are two type
# instance variable
# class variable 

class mobile:
    # class variable
    fp='Yes'

    # class method
    @classmethod
    def is_fp(cls):
        print(cls.fp)
 
    # instance variable
    def __init__(self):  
        self.model='iphone'

    def show_model(self):
        print(self.model) 

obj=mobile()
## class variable outside class
mobile.is_fp()

## instance variable outside class 
obj.show_model()