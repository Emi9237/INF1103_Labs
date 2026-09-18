inventory = 0
user_input = ''
rejected = 0

# while user_input != 'quit':
#     if user_input == 'quit':
#         print("Total Deliveries Processed ", inventory)
#         print("Number of Failed/Rejected Entries ", rejected)
#         break

def get_valid_input():
    user_input = input("Enter stock quantity: ")
    if user_input.isdigit():
        return user_input
        # inventory += int(user_input)
        # if inventory > 500:
        #     print("Inventory has exceeded 500 units")
    else:
        rejected += 1
        print("Error: this input is not valid")
        return user_input == "quit"

def process_delivery(current_total, new_value):
    new_value == current_total + int(user_input)