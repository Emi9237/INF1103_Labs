inventory = 0
failed_attempts = 0
deliveries_processed = 0

def get_valid_input():
    user_input = input("Enter stock quantity: ")

    if user_input == "quit":
        return "quit"

    if user_input.isdigit():
        return user_input

    print("Error: this input is not valid")

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed ", total_units)
    print("Number of Failed/Rejected Entries ", failed_attempts)