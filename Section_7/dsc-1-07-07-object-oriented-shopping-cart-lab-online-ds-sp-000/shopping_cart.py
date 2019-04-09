class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.emp_discount = emp_discount
        self.items = []
    def add_item(self, name, price, quantity=1):
        self.items.append([name, price, quantity])
        self.total = 0
        for i in range(len(self.items)):
            self.total += self.items[i][1] * self.items[i][2]
        return self.total
    def mean_item_price(self):
        quant = 0
        for i in range(len(self.items)):
            quant += self.items[i][2]
        total = self.total
        mean = total/quant
        return mean

    def median_item_price(self):
        pass

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass