from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    # Constructor
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    # Getters
    def get_weight(self):
        return self.__weight

    # Methods
    def display_information(self):
        super().display_information()
        print(f" | Weight: {self.__weight}kg")

    def get_fulfillment_info(self):
        return "This product will require physical shipping."

    def calculate_shipping_cost(self):
       print(f"Shipping cost: ${self.__weight * 6.20:.2f}")