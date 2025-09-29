#region IMPORTS
import os

#endregion


#region INIT DATA
company = {
    'id': 1,
    'name': 'ABC Software d.o.o.',
    'tax_id': '01234567890',
    'hq': {
        'street': 'Duga ulica 15',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Hrvatska'
    },
    'email': 'info@abc-software.hr'
}

bank = {
    'id': 1,
    'name': 'Lipa po lipa d.d.',
    'hq': {
        'street': 'Kratka ulica 5',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Hrvatska'
    }
}

currency = {
    'id': 1,
    'name': 'Euro',
    'symbol': '€',
    'code': 'EUR'
}

transactions = []

bank_account = {
    'id': 1,
    'IBAN': 'HR45875465481354654',
    'balance': 0.00,
    'opening_date': '2025-09-29',
    'bank': bank,
    'currency': currency,
    'transactions': transactions
}

#endregion


#region MAIN MENU
def clear_display() -> None:
    os.system('cls') if os.name == 'nt' else os.system('clear')

def main_menu():
    while True:
        clear_display()
        print('\t== BANK MANAGER ==')
        print()
        print('MENU:')
        print()
        print('1. OPENING AN ACCOUNT ')
        print('2. I HAVE AN ACCOUNT ')
        print('0. EXIT')

        menu_items = input('Ennter a number of functionality you want: ')

        if menu_items.isdigit():
            return int(menu_items)
        else: 
            print('Invalid entry! Please try again. ')
            input('To make a new selection, press the ENTER key.')
#endregion

#region FUNCTIONS
def opening_an_account():
    pass
def existing_account():
    pass
#endregion

#region KEY FUNCTIONS
def main():
    menu_item = main_menu()

    if menu_item == 0:
        print()
        print('Thanks for using Bank manager App! ')
        return
    elif menu_item == 1:
        opening_an_account()
        print()
        input('Press ENTER to continue!')
    elif menu_item == 2:
        existing_account()
        print()
        input('Press ENTER to continue!')
    else:
        print(menu_item)
        input()
#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    main()
#endregion