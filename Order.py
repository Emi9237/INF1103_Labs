from OrderLine import OrderLine
from Product import Product

class Order():
    # Constructor
    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []

    # Getters
    def get_order_id(self) -> str:
        return self.order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self.order_lines

    # Methods
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> None:
        del self.order_lines[index]

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def display(self) -> None:
        print(f"Order {self.order_id}:")
        for line in self.order_lines:
            print(f"    Product: {line.get_product().get_name()}, Qty: {line.get_quantity()}, Subtotal: {line.calculate_subtotal()}")
        print(f"    Total: {self.calculate_total()}")