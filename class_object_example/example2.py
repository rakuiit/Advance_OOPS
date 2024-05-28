class Mobile:
    def __init__(self):
        self.model="realme"

    def show_model(self):
        print("Model is ",self.model)

x=Mobile()
x.show_model()

print(x.model)
x.model="iphone"
print(x.model)
x.show_model()