class Good:
    def __init__(self, id : int, name: str, price: float) -> None:
        self.id = id
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f"id: {self.id} name: {self.name} price: {self.price}"
