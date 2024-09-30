
class PaymentSystem:
    def process_payment(self, amount, method):
        if method.lower() == "online":
            print(f"Processing online payment of ${amount:.2f}...")
        
            print("Online payment successful!")
        else:
            print(f"Please pay ${amount:.2f} in cash.")
            print("Cash payment successful!")