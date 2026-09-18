user_input = ""
new_value = 0

def get_valid_input():
    rejected = 0

    user_input = input("Enter stock quantity: ")

    if user_input.isdigit() & int(user_input) >= 0:
        return user_input
    else:
        rejected += 1
        print("Error: this input is not valid")
        return user_input == "quit"

def process_delivery(current_total, new_value):
    new_value = current_total + int(user_input)
    return new_value

def calculate_tax(amount):
    amount = new_value * 1/10
    return amount

def generate_report(total_units, failed_attempts):
    if user_input == 'quit':
        print("Total Deliveries Processed ", total_units)
        print("Number of Failed/Rejected Entries ", failed_attempts)

get_valid_input()