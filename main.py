import json
from Product import Product
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from OrderLine import OrderLine

FILE_NAME = "inventory.json"


def load_inventory():
    inventory = Inventory()
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\ninventory.json not found.")
        print("An empty inventory is created.")
        return inventory

    print("\ninventory.json found.")
    for item in data:
        if item.get("Type") == "physical":
            product = PhysicalProduct(item["ID"], item["Name"], float(str(item["Price"]).replace("$", "")), int(item["Stock"]), float(item["Weight"]))
        else:
            product = DigitalProduct(item["ID"], item["Name"], float(str(item["Price"]).replace("$", "")), int(item["Stock"]), item["Download_Size"])
        inventory.add_product(product)
    print("Inventory loaded successfully.")
    return inventory


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        item = {
            "ID": product.get_product_id(),
            "Name": product.get_name(),
            "Price": product.get_price(),
            "Stock": product.get_stock()
        }
        if isinstance(product, PhysicalProduct):
            item["Type"] = "physical"
            item["Weight"] = product.get_weight()
        elif isinstance(product, DigitalProduct):
            item["Type"] = "digital"
            item["Download_Size"] = product.get_download_size()
        data.append(item)
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def read_number(prompt, label, cast):
    while True:
        text = input(prompt).replace("$", "").strip()
        if text == "":
            print(f"\nPlease input a {label}.\n")
            continue
        try:
            value = cast(text)
        except ValueError:
            print(f"\nPlease enter a valid number for {label}.\n")
            continue
        if value < 0:
            print(f"\nNegative numbers are not valid. Please input a valid {label}.\n")
            continue
        return value

def add_product_menu(inventory):
    print("\nAdd New Product")

    while True:
        product_type = input("Select a product type, physical or digital: ").strip().lower()
        if product_type == "":
            print("\nPlease input a Product Type.\n")
        elif product_type not in ("physical", "digital"):
            print("\nPlease enter 'physical' or 'digital'.\n")
        else:
            break

    while True:
        product_id = input("Product ID: ")
        if product_id == "":
            print("\nPlease input a Product ID.\n")
        elif not product_id.startswith("P"):
            print("\nProduct ID must start with a 'P'. Please input a different Product ID.\n")
        elif inventory.search_product(product_id) is not None:
            print(f"\nProduct ID: {product_id} already exists. Please input a different Product ID.\n")
        else:
            break

    while True:
        name = input("Product Name: ")
        if name == "":
            print("\nPlease input a Product Name.\n")
        else:
            break

    price = read_number("Price: ", "Price", float)
    stock = read_number("Stock Quantity: ", "Stock quantity", int)

    if product_type == "physical":
        weight = read_number("Weight: ", "Weight", float)
        product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = read_number("Download Size: ", "Download Size", float)
        product = DigitalProduct(product_id, name, price, stock, download_size)

    inventory.add_product(product)
    print("\nProduct added successfully!")

def update_stock_menu(inventory):
    print("\nUpdate Stock")
    while True:
        product_id = input("Enter Product ID: ")
        if product_id == "":
            print("\nPlease input a Product ID.\n")
            continue
        elif inventory.search_product(product_id) is None:
            print("\nProduct not found.\n")
        else:
            break

    product = inventory.search_product(product_id)

    print(f"\nProduct Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}\n")
    quantity = read_number("New Stock Quantity: ", "Stock quantity", int)
    product.update_stock(quantity)
    print("\nStock updated successfully!")

def search_product_menu(inventory):
    print("\nSearch Product")

    while True:
        product_id = input("Enter Product ID: ")
        if product_id == "":
            print("\nPlease input a Product ID.\n")
        elif not product_id.startswith("P"):
            print("\nProduct ID must start with a 'P'. Please input a different Product ID.\n")
        else:
            break

    product = inventory.search_product(product_id)
    
    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-----------------------------------------------------------------------------------")
    product.display_information()
    print("-----------------------------------------------------------------------------------")


def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    inventory = load_inventory()
    display_menu()

    while True:
        user_input = input("\nEnter option: ")

        if user_input == "1":
            inventory.display_all()
        elif user_input == "2":
            add_product_menu(inventory)
        elif user_input == "3":
            update_stock_menu(inventory)
        elif user_input == "4":
            search_product_menu(inventory)
        elif user_input == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif user_input == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("\nInvalid option. Please enter a number from 1 to 6.")

main()