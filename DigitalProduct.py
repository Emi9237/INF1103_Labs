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
        super().display_information()
        print(f" | Download Size: {self.__download_size}kb")

    def get_fulfillment_info(self):
        return "This product will be delivered digitally."