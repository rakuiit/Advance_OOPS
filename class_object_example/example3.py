class Mobile:
    def __init__(self,model):
        self.model=model

    def show_model(self,price):
        self.price=price
        print("Model is",self.model,"and price is",self.price )

x=Mobile("Realme")
x.show_model(1000)

