from Product import Product

class OrderLine():
    # Constructor
    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity = quantity

    # Getters
    def get_product(self) -> Product:
        return self.product

    def get_quantity(self) -> int:
        return self.quantity

    # Methods
    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity