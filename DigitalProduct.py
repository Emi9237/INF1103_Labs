from Product import Product

class DigitalProduct(Product):

    # Constructor
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    # Getters
    def get_download_size(self):
        return self.__download_size

    # Methods
    def display_information(self):
        print(f"ID: {self.get_product_id()} | Name: {self.get_name()} | Price: ${self.get_price():.2f} | Stock: {self.get_stock()} | Download Size: {self.__download_size}")