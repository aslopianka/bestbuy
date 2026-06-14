import products
import store
import sys

from products import Product

# set up initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store_instance):
    display_menu()


def display_menu():
    """ Displays menu and title """
    print('         Store Menu')
    print('------------------------------')
    print('1. List all products in store')
    print('2. Show total amount in store')
    print('3. Make an order')
    print('4. Quit')


def quit_program():
    """ Ends the program gracefully with a message."""
    print('\n Good bye!')
    sys.exit()


def get_order_input(items_in_store):
    still_ordering = True
    selected_products = []

    while still_ordering:
        print("When you want to finish order, enter empty text.")
        product_number_to_add = input("Which product # do you want?")

        if not product_number_to_add or product_number_to_add == "":
            return selected_products

        try:
            product_number_to_add = int(product_number_to_add)
        except ValueError as e:
            print("Please enter a valid integer that represents a product form the list.")
            continue


def list_all_items():
    all_products = best_buy.get_all_products()

    print("----")
    for index, product in enumerate(all_products, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("----")

    return None

def show_total_amount_in_store():
    total_amount = best_buy.get_total_quantity()
    print(f"\n Total of {total_amount} items in store.")

    return None


def get_corresponding_action(menu_choice):
    """Returns the action callable for the given menu choice."""
    actions = {
        1: list_all_items,
        2: show_total_amount_in_store,
        3: process_order,
        4: quit_program
    }

    if menu_choice not in actions:
        raise ValueError("Invalid choice")

    return actions[menu_choice]


def process_order():
    # should show all items with numbers
    items_in_store = best_buy.get_all_products()
    for item in items_in_store:
        item.show()

    ordered_items = get_order_input(items_in_store)
    print(ordered_items)
    # should add selected item to cart -> call product.buy
    # when empty input added -> return card and call store.order with cart content
    return [('item1', 1),('item2', 2)]


def main():
    """ Main function to run the main application. """
    while True:
        start(best_buy)
        menu_selection = input("Please choose a number:")

        try:
            users_choice = int(menu_selection)
        except ValueError:
            print("\n Invalid choice. Please only enter a number between 1 and 9.")
            continue

        try:
            action = get_corresponding_action(users_choice)
            result = action()
            if result:
                print(result)

        except (ValueError, KeyError, TypeError) as e:
            print(e)
            continue





if __name__ == '__main__':
    main()