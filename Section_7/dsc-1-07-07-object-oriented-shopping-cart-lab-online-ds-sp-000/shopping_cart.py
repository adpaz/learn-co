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
        
        length = 0
        for i in range(len(self.items)):
            length += self.items[i][2]
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (prices[mid_one] + prices[mid_two])/2
            return median
        mid = int(length/2)
        return self.items[mid][1]

    def apply_discount(self):
        if (self.emp_discount == None):
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self.total*0.8

    def void_last_item(self):
        if self.items:
            self.items.pop()
        else:
            return "no items"
        self.total = 0
        for i in range(len(self.items)):
            self.total += self.items[i][1] * self.items[i][2]
        return self.total