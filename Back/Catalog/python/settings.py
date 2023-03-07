class Product:

    def __init__(self, id_product: int, stock: int, price: int, name: str):
        self.id_product = id_product
        self.stock = stock
        self.price = price
        self.name = name

    def set_id_product(self, id_product: int) -> None:
        self.id_product = id_product


    def get_id_product(self) -> int:
        return self.id_product
    
    def set_stock(self, stock: int) -> None:
        self.stock = stock


    def get_stock(self) -> int:
        return self.stock
    
    def set_price(self, price: int) -> None:
        self.price = price


    def get_price(self) -> int:
        return self.price

    def set_name(self, name: str) -> None:
        self.name = name


    def get_name(self) -> str:
        return self.name