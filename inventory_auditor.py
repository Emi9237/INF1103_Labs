import json
inventory = []

# Do validation later e.g. same id, existing product
def add_product(inventory):
    print("\nAdd New Product")
    id_input = input("Product ID: ")
    name_input = input("Product Name: ")
    price_input = input("Price: ")
    stock_input = input("Stock Quantity: ")

    inventory.append({
        "ID": id_input,
        "Name": name_input,
        "Price": price_input,
        "Stock": stock_input
    })
    print("\nProduct added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")
    id_input = input("Enter Product ID: ")

    for i in range(len(inventory)):
        if id_input == inventory[i]["ID"]:
            print("\nProduct Found:\nName: " + inventory[i]["Name"] + "\nCurrent Stock: " + inventory[i]["Stock"])
            new_stock_input = input("\nNew Stock Quantity: ")
            inventory[i]["Stock"] = new_stock_input
    print("\nStock updated successfully!")

def search_product(inventory):
    print("\nSearch Product")
    id_input = input("Enter Product ID: ")
    
    for i in range(len(inventory)):
        if id_input == inventory[i]["ID"]:
            print("\nProduct Found")
            print("------------------------------------------------")
            print("ID: " + inventory[i]["ID"] + "\nName: " + inventory[i]["Name"] + "\nPrice: " + inventory[i]["Price"] + "\nStock: " + inventory[i]["Stock"])
            print("------------------------------------------------")

def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")
    # for i in range(len(inventory)):
    for product in inventory:
        print("ID: " + product["ID"] + " | Name: " + product["Name"] + " | Price: " + product["Price"] + " | Stock: " + product["Stock"])
    print("------------------------------------------------")

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("\ninventory.json found.")
            print("Inventory loaded successfully.")
    except:
        inventory = []
        print("\ninventory.json not found.")
        print("An empty inventory is created.")
    return inventory

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = load_inventory()
display_menu()

while True:
    user_input = input("\nEnter option: ")
    
    if user_input == "1":
        display_all(inventory)
    elif user_input == "2":
        add_product(inventory)
    elif user_input == "3":
        update_stock(inventory)
    elif user_input == "4":
        search_product(inventory)
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