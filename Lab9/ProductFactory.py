from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float = None, download_size: float = None) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock, weight, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock, download_size, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")