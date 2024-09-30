from authenticate import UserAuthentication
from food_item import FoodItem, Deal
from menu import FoodMenu, DealMenu
from ordering import Order
from payment import PaymentSystem

import csv

class FoodOrderingSystem:
    def __init__(self, users_file):
        self.auth = UserAuthentication(users_file)
        self.food_menu = FoodMenu()
        self.deal_menu = DealMenu()
        self.order = Order()
        self.payment = PaymentSystem()
        self.setup_menu('menu.csv')
        self.setup_deals('deals.csv')
    
    def setup_menu(self, menu_file):
        with open(menu_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price = row
                self.food_menu.add_item(FoodItem(name, float(price)))

    def setup_deals(self, deals_file):
        with open(deals_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price, items = row
                items_list = items.split(';')
                self.deal_menu.add_deal(Deal(name, float(price), items_list))

    def run(self):
        print("Welcome to Mayer Hassan Fooding System")
        while True:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.auth.register(username, password)
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if self.auth.login(username, password):
                    print("Login successful!")
                    self.show_options()
                    break
                else:
                    print("Invalid username or password.")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_options(self):
        while True:
            print("\n1. View Food Items\n2. View Deals\n3. Checkout\n4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.food_menu.display_menu()
                item_number = input("\nEnter the number of the item to order (or 'back' to go back): ")
                if item_number.lower() == 'back':
                    continue
                else:
                    try:
                        item_index = int(item_number) - 1
                        item = self.food_menu.items[item_index]
                        self.order.add_to_order(item)
                    except (ValueError, IndexError):
                        print("Invalid item number. Please try again.")
            elif choice == "2":
                self.deal_menu.display_deals()
                deal_number = input("\nEnter the number of the deal to order (or 'back' to go back): ")
                if deal_number.lower() == 'back':
                    continue
                else:
                    try:
                        deal_index = int(deal_number) - 1
                        deal = self.deal_menu.deals[deal_index]
                        self.order.add_to_order(deal)
                    except (ValueError, IndexError):
                        print("Invalid deal number. Please try again.")
            elif choice == "3":
                total = self.order.display_order()
                payment_method = input("Do you want to pay by cash or online? ")
                self.payment.process_payment(total, payment_method)
                break
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
