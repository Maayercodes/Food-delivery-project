from food_ordering_system import FoodOrderingSystem

users_file = 'users.csv'
open(users_file, 'a').close()

system = FoodOrderingSystem(users_file)
system.run()

