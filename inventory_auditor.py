import json
inventory = []

def add_product(inventory):
    print("\nAdd New Product")
    
    while True:
        id_input = input("Product ID: ")

        if id_input == "":
            print("\nPlease input a Product ID.\n")
            continue
        if not id_input.startswith("P"):
            print("\nProduct ID must start with a 'P'. Please input a different Product ID.\n")
            continue
        for i in range(len(inventory)):
            if id_input == inventory[i]["ID"]:
                print("\nProduct ID: " + id_input + " already exists. Please input a different Product ID.")
                break
        else:
            break

    while True:
        name_input = input("Product Name: ")
        if name_input == "":
            print("\nPlease input a Product Name.\n")
            continue
        else:
            break

    while True:
        price_input = input("Price: ").replace("$", "")
        if price_input == "":
            print("\nPlease input a Price.\n")
            continue
        elif float(price_input) < 0:
            print("\nNegative numbers are not valid. Please input a valid Price.\n")
            continue
        else:
            break

    while True:
        stock_input = input("Stock Quantity: ")
        if stock_input == "":
            print("\nPlease input a Stock quantity.\n")
            continue
        elif int(stock_input) < 0:
            print("\nNegative numbers are not valid. Please input a valid Stock quantity.\n")
            continue
        else:
            break

    inventory.append({
        "ID": id_input,
        "Name": name_input,
        "Price": "$" + price_input,
        "Stock": stock_input
    })
    print("\nProduct added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")

    while True:
        id_input = input("Enter Product ID: ")

        if id_input == "":
            print("\nPlease input a Product ID.\n")
            continue

        for i in range(len(inventory)):
            if id_input == inventory[i]["ID"]:
                print("\nProduct Found:\nName: " + inventory[i]["Name"] + "\nCurrent Stock: " + inventory[i]["Stock"])

                while True:
                    new_stock_input = input("\nNew Stock Quantity: ")
                    if new_stock_input == "":
                        print("\nPlease input a Stock quantity.\n")
                    elif int(new_stock_input) < 0:
                        print("\nNegative numbers are not valid. Please input a valid Stock quantity.\n")
                    else:
                        break

                inventory[i]["Stock"] = new_stock_input
                print("\nStock updated successfully!")
                break
        else:
            print("\nProduct not found.\n")
            continue
        break 

def search_product(inventory):
    print("\nSearch Product")

    while True:
        id_input = input("Enter Product ID: ")

        if id_input == "":
            print("\nPlease input a Product ID.\n")
            continue
        elif not id_input.startswith('P'):
            print("\nProduct ID must start with a 'P'. Please input a different Product ID.\n")
            continue

        for i in range(len(inventory)):
            if id_input == inventory[i]["ID"]:
                print("\nProduct Found")
                print("------------------------------------------------")
                print("ID: " + inventory[i]["ID"] + "\nName: " + inventory[i]["Name"] + "\nPrice: " + inventory[i]["Price"] + "\nStock: " + inventory[i]["Stock"])
                print("------------------------------------------------")
                break
        else:
            print("\nProduct not found.\n")
            continue
        break

def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")
    if len(inventory) == 0:
        print("There are no products in the inventory.")
    else:
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