import logging
import random
import threading


logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] (%(threadName)-s) ($(module)-s) (%(funcName)-s) $(message)s', filename='/tmp/locking-py.log')


class Repository:
    def __init__(self):
        self.repo = {}
        self.lock = threading.Lock()


    def create(self, entry):
        logging.info("waiting for lock")
        self.lock.acquire()
        try:
            logging.info("acquired lock")
            new_id = len(self.repo.keys())
            entry["id"] = new_id
            self.repo[new_id] = entry
        finally:
            logging.info("releasing lock")
            self.lock.release()

    def find(self, entry_id):
        logging.info("waiting for lock")
        self.lock.acquire()
        try:
            logging.info("acquired lock")
            return self.repo[entry_id]
        except KeyError:
            return None
        finally:
            logging.info("releasing lock")
            self.lock.release()
    
    def all(self):
        logging.info("waiting for lock")
        self.lock.acquire()
        try:
            logging.info("acquired lock")
            return self.repo
        finally:
            logging.info("releasing lock")
            self.lock.release()


class ProductRepository(Repository):
    def __init__(self):
        Repository.__init__(self)

    def add_product(self, description, price):
        self.create({"description": description, "price": price})


class PurcharseRepository(Repository):
    def __init__(self, product_repository):
        Repository.__init__(self)
        self.product_repository = product_repository

    def add_purchase(self, product_id, qty):
        product = self.product_repository.find(product_id)
        if product is not None:
            total_amount = product["price"] * qty
            self.create({"product_id": product_id, "qty": qty, "total_amount": total_amount})

    def sales_by_product(self, product_id):
        sales = {"product_id": product_id, "qty": 0, "total_amount": 0}
        all_purchases = self.all()
        for k in all_purchases:
            purchase = all_purchases[k]
            if purchase["product_id"] == sales["product_id"]:
                sales["qty"] += purchase["qty"]
                sales["total_amount"] += purchase["total_amount"]
        return sales

class Buyer(threading.Thread):
    def __init__(self, name, product_repository, purchase_repository):
        """
        Initializes Buyer class object
        Manages threads
        """
        threading.Thread.__init__(self, name="Buyer-" + name)
        self.product_repository = product_repository
        self.purchase_repository =purchase_repository

    def run(self):
        for i in range(0, 1000):
            max_product_id = len(self.product_repository.all().keys())
            product_id = random.randrange(0, max_product_id +1, 1)
            qty = random.randrange(0, 100, 1)
            self.purchase_repository.add_purchsase(product_id, qty)


class ProviderAuditor(threading.Thread):
    