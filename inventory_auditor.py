import json

# Do validation later e.g. same id, existing product
inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": "$1200.00", "Stock": "15"},
    {"ID": "P002", "Name": "Mouse", "Price": "$25.50", "Stock": "40"},
    {"ID": "P003", "Name": "Keyboard", "Price": "$45.00", "Stock": "25"}
]

def add_product():
    print("\nAdd New Product\n")
    id_input = input("\nProduct ID: ")
    name_input = input("\nProduct Name: ")
    price_input = input("\nPrice: ")
    stock_input = input("\nStock Quantity: ")

    inventory.append = ({
        "ID": id_input,
        "Name": name_input,
        "Price": price_input,
        "Stock": stock_input
    })

    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
        print("\nProduct added successfully!\n")