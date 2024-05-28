class Mobile:
    # constructor
    def __init__(self,model,volumn=10):
        self.model=model
        self.volumn=volumn
    
    def show_model(self,price):
        self.price=price
        print("The model is", self.model,"and volumn is",self.volumn,"and price is",self.price)


# passing arg to constructor 
obj=Mobile("iphone",20)
# accessing method outside the class
obj.show_model(50000)
