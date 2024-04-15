def display_menu(drinks):
    print("Welcome to the Vending Machine!")
    print("Here are the available drinks:")
    for index, (drink, price) in enumerate(drinks.items(), start=1):
        print(f"{index}. {drink}: ${price:.2f}")

def select_drink(drinks):
    while True:
        try:
            choice = int(input("Please enter the number for your drink choice: "))
            print(f"\nYour choice: {choice}")
            if 1 <= choice <= len(drinks):
                return list(drinks.keys())[choice - 1]
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def accept_payment(price):
    valid_denominations = [1, 5, 10, 20, 50, 100]
    total_payment = 0

    while total_payment < price:
        try:
            note = int(input("Please insert your payment in dollar notes (1, 5, 10, 20, 50, 100): $"))
            if note not in valid_denominations:
                print("Invalid note.")
                continue
            total_payment += note
            print(f"Total payment: ${total_payment}")
        except ValueError:
            print("Invalid input. Please enter a valid note.")

    return total_payment

def calculate_change(payment, price):
    return payment - price

def return_change(change):
    print("Here is your change:")
    remaining_change = change
    while remaining_change > 0:
        if remaining_change >= 100:
            num_notes = remaining_change // 100
            print(f"{int(num_notes)}x $100 notes")
            remaining_change %= 100
        elif remaining_change >= 50:
            num_notes = remaining_change // 50
            print(f"{int(num_notes)}x $50 notes")
            remaining_change %= 50
        elif remaining_change >= 20:
            num_notes = remaining_change // 20
            print(f"{int(num_notes)}x $20 notes")
            remaining_change %= 20
        elif remaining_change >= 10:
            num_notes = remaining_change // 10
            print(f"{int(num_notes)}x $10 notes")
            remaining_change %= 10
        elif remaining_change >= 5:
            num_notes = remaining_change // 5
            print(f"{int(num_notes)}x $5 notes")
            remaining_change %= 5
        else:
            print(f"{int(remaining_change)}x $1 notes")
            remaining_change = 0


def complete_transaction(drink):
    print(f"Here is your {drink}. Enjoy!")

def repeat_or_exit():
    while True:
        choice = input("Would you like to make another purchase? (yes/no): ").lower().strip()
        if choice == "yes" or choice == "no":
            return choice == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def vending_machine(drinks):
    while True:
        display_menu(drinks)
        selected_drink = select_drink(drinks)
        price = drinks[selected_drink]
        print(f"You've selected: {selected_drink} - ${price:.2f}")
        payment = accept_payment(price)
        change = calculate_change(payment, price)
        if change < 0:
            print("Insufficient payment. I need more money.")
            continue
        elif change == 0:
            complete_transaction(selected_drink)
        else:
            return_change(change)
            complete_transaction(selected_drink)
        if not repeat_or_exit():
            break

# Sample drinks and prices
drinks = {"Milo Ais": 3.00, "Teh Ais": 1.00, "Sirap Ais": 7.00}

# Run the vending machine
vending_machine(drinks)
