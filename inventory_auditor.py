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

def update_stock():
    print("\nUpdate Stock\n")
    id_input = input("\nEnter Product ID: ")

    for i in range(len(inventory)):
        if id_input == inventory[i]["ID"]:
            print("\nProduct Found:\n Name: " + inventory[i]["Name"] + "\nCurrent Stock: " + inventory[i]["Stock"])
            new_stock_input = input("\nNew Stock Quantity: ")
            inventory[i]["Stock"] = new_stock_input

    with open("inventory.json", "a") as file:
        json.dumps(inventory, file)
        print("\nStock updated successfully!\n")

def search_product():
    print("\nSearch Product\n")
    id_input = input("\nEnter Product ID: ")
    
    for product in range(len(inventory)):
        if id_input == product[0]:
            print("\n\nProduct Found:")
            print("------------------------------------------------")
            print("ID: " + product[0] + "\nName: " + product[1] + "\nPrice: " + product[2] + "\nStock: " + product[3])
            print("------------------------------------------------")
    
    new_stock_input = input("\nNew Stock Quantity: ")
    
    with open("inventory.json", "a") as file:
        json.dumps(inventory, file)
        print("\nStock updated successfully!\n")