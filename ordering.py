class Order:
    def __init__(self):
        self.items = []

    def add_to_order(self, item):
        self.items.append(item)

    def display_order(self):
        print("Your order:")
        total = 0
        for item in self.items:
            print(item)
            total += item.price
        print(f"Total: ${total:.2f}")
        return total
