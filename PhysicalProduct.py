from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    SHIPPING_RATE_PER_KG = 6.20
    # Constructor
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    # Getters
    def get_weight(self) -> float:
        return self.__weight

    # Methods
    def display_information(self) -> None:
        super().display_information()
        print(f" | Weight: {self.__weight}kg")

    def get_fulfilment_info(self) -> str:
        return "This product will require physical shipping."

    def calculate_shipping_cost(self) -> float:
       return self.__weight * PhysicalProduct.SHIPPING_RATE_PER_KG