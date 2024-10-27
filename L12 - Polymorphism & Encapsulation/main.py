class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def show(self):
        print("You have deposited successfully")

class POS:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def show(self):
        print("You have withdrawn successfully")

Uba = Bank("UBA", "Lagos")
Moses = POS("Moses", "Lagos")

for m in (Uba, Moses):
    m.show()

class Computer:
    def __init__(self):
        self.__price = 500

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price


comp1 = Computer()
comp1.set_price(800)
print(comp1.get_price())