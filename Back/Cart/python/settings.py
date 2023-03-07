class Product:

    def __init__(self, id_product: int, quantity: int, individual_price: int, name: str):
        self.id_product = id_product
        self.quantity = quantity
        self.individual_price = individual_price
        self.name = name

    def set_id_product(self, id_product: int) -> None:
        self.id_product = id_product


    def get_id_product(self) -> int:
        return self.id_product
    
    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity


    def get_quantity(self) -> int:
        return self.quantity
    
    def set_individual_price(self, individual_price: int) -> None:
        self.individual_price = individual_price


    def get_individual_price(self) -> int:
        return self.individual_price
    
    def set_name(self, name: str) -> None:
        self.name = name


    def get_name(self) -> str:
        return self.name