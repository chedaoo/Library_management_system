# check.py
from models import Checkout
import storage

class CheckoutManager:
    def __init__(self):
        self.checkouts = storage.load_checkouts()

    def checkout_book(self, user_id, isbn):
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        storage.save_checkouts(self.checkouts)
        
    def list_checkouts(self):
        for checkout in self.checkouts:
            print(checkout)