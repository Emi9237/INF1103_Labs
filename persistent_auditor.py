inventory = 0
failed_attempts = 0
deliveries_processed = 0
new_transaction = []
old_transactions = []
old_total = 0

def get_valid_input():
    global failed_attempts
    global new_transaction

    while True:
        user_input = input("Enter stock quantity or 'quit': ")

        if user_input == "quit":
            return "quit"

        elif user_input.isdigit():
            new_transaction.append(user_input)
            print(new_transaction)
            return int(user_input)

        else:
            failed_attempts += 1
            print("Error: this input is not valid")

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("\nTotal Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

def load_inventory():
    global old_transactions
    global old_total

    try:
        with open("inventory.txt", "r") as file:
            inventory = file.readlines()

            if len(inventory) == 0:
                old_transactions = []
                old_total = 0
            else:
                old_transactions = inventory[0]
                old_total = inventory[1]

            print(inventory)
    except:
        with open("inventory.txt", "x") as file:
            print("A new inventory file is created.")

def save_inventory(new_transaction, total_units):
    global old_transactions
    global old_total

    if old_transactions != []:

        old_transactions = old_transactions.replace("Transaction history list: ", "")
        old_transactions = old_transactions.strip()
        old_transactions = old_transactions.strip("[]")

        if old_transactions:
            old_transactions = old_transactions.split(", ")

            for i in range(len(old_transactions)):
                old_transactions[i] = old_transactions[i].strip("'\"")

        old_total = old_total.replace("Final total: ", "")
        old_total = int(old_total.strip())

    else:
        old_total = 0

    old_transactions.extend(new_transaction)

    new_total = old_total + total_units

    with open("inventory.txt", "w") as file:
        file.write("Transaction history list: " + str(old_transactions) + "\n")
        file.write("Final total: " + str(new_total))

load_inventory()

while True:
    user_input = get_valid_input()

    if user_input == "quit":
        generate_report(deliveries_processed, failed_attempts)
        save_inventory(new_transaction, deliveries_processed)
        break

    inventory = process_delivery(inventory, user_input)

    tax = calculate_tax(user_input)

    deliveries_processed += 1

    if inventory > 500:
        print("Inventory has exceeded 500 units")
        break