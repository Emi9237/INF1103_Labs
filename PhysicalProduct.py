from Product import Product

class PhysicalProduct(Product):

    # Constructor
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    # Getters
    def get_weight(self):
        return self.__weight

    # Methods
    def display_information(self):
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | Price: ${self.get_price()} | Stock: {self.get_stock()} | Weight: {self.__weight}")