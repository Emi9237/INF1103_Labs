import os
import sys
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DiscountStrategy import DiscountStrategy, NoDiscount, PercentageDiscount, BulkDiscount
from Inventory import Inventory
from Order import Order
from OrderLine import OrderLine
from Product import Product
from ProductFactory import ProductFactory
from Supplier import Supplier
from main import get_positive_float, load_products

CSV = """product_type,product_id,name,price,stock_quantity
        physical,P001,Desk Lamp,25.00,10
        digital,D001,Photo Editor,49.90,100
        service,S001,Installation,30.00,5
        physical,P002,Office Chair,abc,3
        physical,P003,Monitor Stand,39.50,7
        """

class HalfPrice(DiscountStrategy):  # brand-new strategy, defined without touching Order
    def apply(self, total: float) -> float:
        return total / 2

class TestStrategy(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S1", "Test", "t@example.com")
        self.order = Order("O1", BulkDiscount(200, 20))
        self.order.add_order_line(ProductFactory.create("physical", "P1", "Item", 125.0, 10, self.supplier), 2)  # total 250

    def test_total_uses_strategy(self):
        self.assertAlmostEqual(self.order.calculate_total(), 230)

    def test_default_is_no_discount(self):
        self.assertIsInstance(Order("O2").discount, NoDiscount)

    def test_set_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(self.order.calculate_total(), 225)

    def test_new_strategy_without_changing_order(self):
        self.order.set_discount(HalfPrice())
        self.assertAlmostEqual(self.order.calculate_total(), 125)

class TestFactory(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S1", "Test", "t@example.com")

    def test_creates_products(self):
        for kind in ("physical", "digital"):
            self.assertIsInstance(ProductFactory.create(kind, "P1", "Item", 10.0, 1, self.supplier), Product)

    def test_unknown_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S1", "Install", 30.0, 5, self.supplier)

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S1", "Test", "t@example.com")

    def test_invalid_price(self):
        for price in (0, -5):
            with self.assertRaises(ValueError):
                ProductFactory.create("physical", "P1", "Item", price, 1, self.supplier)

    def test_negative_stock(self):
        for kind in ("physical", "digital"):
            with self.assertRaises(ValueError):
                ProductFactory.create(kind, "P1", "Item", 10.0, -1, self.supplier)

    def test_invalid_order_quantity(self):
        product = ProductFactory.create("physical", "P1", "Item", 10.0, 1, self.supplier)
        for qty in (0, -1):
            with self.assertRaises(ValueError):
                OrderLine(product, qty)

class TestExceptionHandling(unittest.TestCase):
    def test_invalid_input_asks_again(self):
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), patch("sys.stdout", new_callable=StringIO) as out:
            self.assertEqual(get_positive_float("Price: "), 12.5)
        self.assertIn("valid number", out.getvalue())
        self.assertIn("greater than zero", out.getvalue())

    def test_missing_file(self):
        with patch("sys.stdout", new_callable=StringIO) as out:
            load_products("missing.csv", Inventory(), None)
        self.assertIn("Products file not found", out.getvalue())
        self.assertIn("Load attempt finished.", out.getvalue())

    def test_bad_rows_skipped(self):
        inventory = Inventory()
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")
            with open(path, "w", newline="") as f:
                f.write(CSV)
            with patch("sys.stdout", new_callable=StringIO) as out:
                load_products(path, inventory, Supplier("S1", "Test", "t@example.com"))
        self.assertEqual(len(inventory.get_products()), 3)
        self.assertIn("3 products loaded.", out.getvalue())
        self.assertIn("Load attempt finished.", out.getvalue())

if __name__ == "__main__":
    unittest.main()