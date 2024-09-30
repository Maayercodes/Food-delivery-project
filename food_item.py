class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class MenuItem(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Deal(FoodItem):
    def __init__(self, name, price, items):
        super().__init__(name, price)
        self.items = items

    def __str__(self):
        items_str = ', '.join(self.items)
        return f"{self.name}: ${self.price:.2f} (Includes: {items_str})"