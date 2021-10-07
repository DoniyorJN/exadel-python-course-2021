from Good import *

class Order:
    def __init__(self, order_id : int, order_date: str, client_id: int, goods: list[Good] = []):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.price = 0
        for good in goods:
            self.price += good.price
    def __str__(self) -> str:
        return f"Order id: {self.order_id} Order date: {self.order_date} Client Id: {self.client_id} Goods: {self.goods}  Price: {self.price}"