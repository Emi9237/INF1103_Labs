inventory = 0
failed_attempts = 0
deliveries_processed = 0
new_transaction = []

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
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.readlines()
            print(inventory)
    except:
        with open("inventory.txt", "x") as file:
            print("A new inventory file is created.")

def save_inventory(new_transaction, total_units):
    with open("inventory.txt", "a") as file:
        file.write("Transaction history list: ")
        file.write(new_transaction)
        file.write("\nFinal total: ")
        file.write(total_units)
        file.write("\n \n")

file = load_inventory()

while True:
    user_input = get_valid_input()

    if user_input == "quit":
        generate_report(deliveries_processed, failed_attempts)
        save_inventory(str(new_transaction), str(deliveries_processed))
        break

    inventory = process_delivery(inventory, user_input)

    tax = calculate_tax(user_input)

    deliveries_processed += 1

    if inventory > 500:
        print("Inventory has exceeded 500 units")
        break