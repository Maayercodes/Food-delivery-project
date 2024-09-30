import csv

class UserAuthentication:
    def __init__(self, users_file):
        self.users_file = users_file

    def register(self, username, password):
        with open(self.users_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print("Registration successful!")

    def login(self, username, password):
        with open(self.users_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False