from Product import Product
from Supplier import Supplier

class DigitalProduct(Product, Supplier):
    # Constructor
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    # Getters
    def get_download_size(self) -> float:
        return self.__download_size

    # Methods
    def display_information(self) -> None:
        super().display_information()
        print(f" | Download Size: {self.__download_size}MB")

    def get_fulfilment_info(self) -> str:
        return "This product will be delivered digitally."