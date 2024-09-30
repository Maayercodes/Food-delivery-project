from food_item import FoodItem, MenuItem, Deal

class FoodMenu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        print("Menu:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")

class DealMenu:
    def __init__(self):
        self.deals = []

    def add_deal(self, deal):
        self.deals.append(deal)

    def display_deals(self):
        print("Deals:")
        for index, deal in enumerate(self.deals, start=1):
            print(f"{index}. {deal}")