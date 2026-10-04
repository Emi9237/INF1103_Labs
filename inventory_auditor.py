import json

# Do validation later e.g. same id, existing product
inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": "$1200.00", "Stock": "15"},
    {"ID": "P002", "Name": "Mouse", "Price": "$25.50", "Stock": "40"},
    {"ID": "P003", "Name": "Keyboard", "Price": "$45.00", "Stock": "25"}
]

def add_product():
    print("\n\nAdd New Product")
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
        print("\n\nProduct added successfully!\n")

def update_stock():
    print("\n\nUpdate Stock")
    id_input = input("\nEnter Product ID: ")

    for i in range(len(inventory)):
        if id_input == inventory[i]["ID"]:
            print("\n\nProduct Found:\n Name: " + inventory[i]["Name"] + "\nCurrent Stock: " + inventory[i]["Stock"])
            new_stock_input = input("\nNew Stock Quantity: ")
            inventory[i]["Stock"] = new_stock_input

    with open("inventory.json", "a") as file:
        json.dumps(inventory, file)
        print("\n\nStock updated successfully!\n")

def search_product():
    print("\n\nSearch Product")
    id_input = input("\nEnter Product ID: ")
    
    for i in range(len(inventory)):
        if id_input == inventory[i]["ID"]:
            print("\n\nProduct Found")
            print("\n------------------------------------------------")
            print("\nID: " + inventory[i]["ID"] + "\nName: " + inventory[i]["Name"] + "\nPrice: " + inventory[i]["Price"] + "\nStock: " + inventory[i]["Stock"])
            print("\n------------------------------------------------")

def display_all():
    print("\n\nCurrent Inventory")
    print("\n------------------------------------------------")
    for i in range(len(inventory)):
        for product in inventory:
            print("\nID: " + product[i]["ID"] + " | Name: " + product[i]["Name"] + " | Price: " + product[i]["Price"] + " | Stock: " + product[i]["Stock"])
    print("\n------------------------------------------------")

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("inventory.json found.")
            print("\nInventory loaded successfully.")
    except:
        inventory = [{}]
        print("\ninventory.json not found.")
        print("\nAn empty inventory is created.")

def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)
        print("\n\nSaving inventory...")
        print("\nInventory saved successfully to inventory.json.")