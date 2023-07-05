class InsufficientFundsError(Exception):
    pass

class AttemptError(Exception):
    pass

def print_items(items):
    print("Here are the available items and their prices:")
    for item, price in items.items():
        print(f"{item}: £{price}")

def get_option():
    option = input("\nEnter the item you want to purchase (You can also input 'exit' to leave): ")
    return option

def validate_option(option, items):
    if option == 'exit':
        print("Thank you for visiting! Goodbye!")
        return False

    if option not in items:
        raise ValueError("Invalid option. Please choose a valid item.")

    return True

def validate_funds(option, customer_money, items):
    if items[option] > customer_money:
        raise InsufficientFundsError("You don't have enough money to purchase this item. Please try to select another item.")

def process_purchase(option, customer_money, items):
    print(f"\nHere's your {option}!")
    customer_money -= items[option]
    print(f"You have £{customer_money} left. Thank you for your purchase!")
    return customer_money

def get_additional_money():
    more_money = input("Do you have more money? Enter the amount or 'no' to leave: ")
    return more_money

def validate_additional_money(more_money):
    if more_money.lower() == 'no':
        print("Thank you for visiting! Goodbye!")
        return False

    try:
        additional_money = int(more_money)
        if additional_money <= 0:
            raise ValueError("Invalid input. Amount should be a positive number.")
        return additional_money
    except ValueError:
        print("Invalid input. Amount should be a number greater than 0.")

def shop_simulation():
    items = {
        'table': 80,
        'bed': 160,
        'storage box': 15,
        'mirror': 25
    }
    customer_money = 100
    attempt_times = 3

    print("Welcome to the shop!")
    print_items(items)

    while True:
        try:
            if attempt_times <= 0:
                raise AttemptError("You have exceeded the maximum purchase attempts. Exiting the shop.")
                break

            option = get_option()

            if not validate_option(option, items):
                break

            if customer_money <= 0:
                print("You don't have any money left. Exiting the shop.")
                break

            validate_funds(option, customer_money, items)

            customer_money = process_purchase(option, customer_money, items)
            break

        except ValueError as e:
            print(str(e))

        except InsufficientFundsError as e:
            attempt_times -= 1
            print(str(e))

            more_money = get_additional_money()

            if not validate_additional_money(more_money):
                break

            additional_money = validate_additional_money(more_money)
            customer_money += additional_money


shop_simulation()
