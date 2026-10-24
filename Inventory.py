class Inventory:

    # Constructor
    def __init__(self):
        self.__products = []

    # Getters
    def get_products(self):
        return self.__products

    # Methods
    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")
        if not self.__products:
            print("There are no products in the inventory.")
        for product in self.__products:
            product.display_information()
        print("------------------------------------------------")