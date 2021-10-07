from Order import *

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add(self, order: Order):
        self.orders.append(order)

    def get(self, order_id): 
        for order in self.orders:
            if order.order_id == order_id:
                return order
        raise "Not Found"

    def list(self, n_latest: int = None):
        if n_latest == None:
            return self.orders
        elif (1 > n_latest) or (n_latest > len(self.orders)) or type(n_latest) != int:
            raise ValueError(f"The value {n_latest} must be an integer in the range [1-{len(self.orders)}]")
        else: 
            return self.orders[-n_latest:]
    def delete(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                return 0
        return "Not found if to delete"