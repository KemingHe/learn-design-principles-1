from coffee import Coffee

class CoffeeWithMilk():
    def __init__(self, amount=0, milk_type=None, cost=0):
        self.amount = amount
        self.milk_type = milk_type
        self.cost = cost
        
    def brew(self):
        print('Brewed milk coffee')
        
    def pour(self):
        print('Poured milk coffee')
        
    def 