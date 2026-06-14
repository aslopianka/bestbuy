import products
import store
import sys

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


def get_corresponding_action(menu_choice):
    """Returns the action callable for the given menu choice."""
    actions = {
        1: best_buy.get_all_products,
        2: best_buy.get_total_quantity,
        3: get_order,
        4: quit_program
    }

    if menu_choice not in actions:
        raise ValueError("Invalid choice")

    return actions[menu_choice]


def get_order():
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
            print(result)

        except (ValueError, KeyError, TypeError) as e:
            print(e)
            continue





if __name__ == '__main__':
    main()