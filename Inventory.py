from Product import Product

class Inventory:

    # Constructor
    def __init__(self) -> None:
        self.products: list[Product] = []

    # Getters
    def get_products(self) -> list[Product]:
        return self.products

    # Methods
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        product = self.search_product(product_id)
        if product is not None:
            self.products.remove(product)
        return product

    def search_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-----------------------------------------------------------------------------------")
        if not self.__products:
            print("There are no products in the inventory.")
        for product in self.__products:
            product.display_information()
        print("-----------------------------------------------------------------------------------")