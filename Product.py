from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    # Constructor
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    # Getters
    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.supplier

    # Methods
    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("\nNegative numbers are not valid. Please input a valid Stock quantity.\n")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock} | Supplier: {self.supplier}" , end="")

    @abstractmethod
    def get_fulfillment_info(self) -> str:
        pass

    def display_supplier_information(self) -> None:
        self.supplier.display_information()