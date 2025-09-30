#region IMPORTS
import os
import time
import random
from datetime import date

#endregion


#region INIT DATA
company = [
    {
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
]

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

bank_account = [
    {
    'id': 1,
    'tax_id': '01234567890',
    'IBAN': 'HR45875465481354654',
    'balance': 0.00,
    'opening_date': '2025-09-29',
    'bank': bank,
    'currency': currency,
    'transactions': transactions
    }
]
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
def get_current_date():
    return date.today().strftime("%d-%m-%Y")

def generate_iban():
    number = ''.join(str(random.randint(0, 9)) for _ in range(19))
    iban = "HR" + number
    return iban

def display_account_info():
    clear_display()
    print("== Account Information ==")
    for acc in bank_account:
        print(f"IBAN: {acc['IBAN']}")
        print(f"Balance: {acc['balance']} {acc['currency']['symbol']}")
        print(f"Currency: {acc['currency']['name']} ({acc['currency']['code']})")
        print("-" * 30)
    input("Press ENTER to return to menu.")

def view_all_transactions():
    clear_display()
    print("== All Transactions ==")
    if not transactions:
        print("No transactions found.")
    else:
        for t in transactions:
            print(f"Company: {t['company']}")
            print(f"IBAN: {t['IBAN']}")
            print(f"Amount: {t['amount']}")
            print(f"Date: {t['date']}")
            print("-" * 30)
    input("Press ENTER to return to menu.")

def deposit_money():
    clear_display()
    print("== Deposit Money ==")
    iban = input("Enter your IBAN: ")
    found = False
    for acc in bank_account:
        if acc['IBAN'] == iban:
            found = True
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    acc['balance'] += amount
                    transaction_entry = {
                        'company': next((c['name'] for c in company if c['tax_id'] == acc['tax_id']), "Unknown"),
                        'IBAN': iban,
                        'amount': f"{amount} EUR",
                        'date': get_current_date()
                    }
                    transactions.append(transaction_entry)
                    print(f"Deposited {amount} EUR to account {iban}.")
            except ValueError:
                print("Invalid amount.")
            break
    if not found:
        print("Account not found.")
    input("Press ENTER to return to menu.")

def withdraw_money():
    clear_display()
    print("== Withdraw Money ==")
    iban = input("Enter your IBAN: ")
    found = False
    for acc in bank_account:
        if acc['IBAN'] == iban:
            found = True
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > acc['balance']:
                    print("Insufficient funds.")
                else:
                    acc['balance'] -= amount
                    transaction_entry = {
                        'company': next((c['name'] for c in company if c['tax_id'] == acc['tax_id']), "Unknown"),
                        'IBAN': iban,
                        'amount': f"-{amount} EUR",
                        'date': get_current_date()
                    }
                    transactions.append(transaction_entry)
                    print(f"Withdrew {amount} EUR from account {iban}.")
            except ValueError:
                print("Invalid amount.")
            break
    if not found:
        print("Account not found.")
    input("Press ENTER to return to menu.")

def account_owner_info():
    clear_display()
    print("== Account Owner Information ==")
    iban = input("Enter your IBAN: ")
    found = False
    for acc in bank_account:
        if acc['IBAN'] == iban:
            found = True
            owner = next((c for c in company if c['tax_id'] == acc['tax_id']), None)
            if owner:
                print(f"Company Name: {owner['name']}")
                print(f"Tax ID: {owner['tax_id']}")
                print(f"Email: {owner['email']}")
                print("Address:")
                print(f"  Street: {owner['hq']['street']}")
                print(f"  Postal Code: {owner['hq']['postal_code']}")
                print(f"  City: {owner['hq']['city']}")
                print(f"  Country: {owner['hq']['country']}")
            else:
                print("Owner information not found.")
            break
    if not found:
        print("Account not found.")
    input("Press ENTER to return to menu.")

def bank_transactions():
    print('bank_transactions() is working!')

    while True:
        clear_display()
        print('\tSelect an option: ')
        print()
        print('1. Display of account information: (balance) and (currency) ')
        print('2. View all transactions - deposits and withdrawals ')
        print('3. Depositing money into an account ')
        print('4. Withdrawing money from the account ')
        print('5. View account owner information ')
        print('0. EXIT')
        print()

        menu_items = input('Ennter a number of functionality you want: ')

        if not menu_items.isdigit():
            print('Invalid entry! Please try again. ')
            input('To make a new selection, press the ENTER key.')
            continue

        menu_items = int(menu_items)

        if menu_items == 0:
            print()
            return  # Exit to previous menu or main menu

        elif menu_items == 1:
            print()
            display_account_info()

        elif menu_items == 2:
            print()
            view_all_transactions()

        elif menu_items == 3:
            print()
            deposit_money()

        elif menu_items == 4:
            print()
            withdraw_money()

        elif menu_items == 5:
            print()
            account_owner_info()

        else:
            print('Invalid entry! Please try again. ')
            input('To make a new selection, press the ENTER key.')





def opening_an_account():
    clear_display()
    while True:
        print()
        new_name = input('Enter a company name: ')
        new_tax_id = input('Enter a tax id : ')
        new_email = input('Enter a email: ')
        new_street = input('Enter a street: ')
        new_postal_code = input('Enter a postal code: ')
        new_city = input('Enter a city: ')
        new_country = input('Enter a country: ')

        new_company = {
            'id': company[-1]['id'] + 1,
            'name': new_name,
            'tax_id': new_tax_id,
            'hq': {
                'street': new_street,
                'postal_code': new_postal_code,
                'city': new_city,
                'country': new_country
            },
            'email': new_email
}
        
        
        company.append(new_company)
        print()
        print('When opening an account, a deposit of at least 500 EUR is required.')
        time.sleep(3)
        clear_display()


        while True:
            payment = int(input('Enter a deposit (min. 500 EUR): '))
            if payment < 500:
                print('You must deposit a minimum amount of 500 euros.')
                continue
            elif payment >= 500:
                transaction_entry = {
                'company': new_name,
                'IBAN': generate_iban(),
                'amount': f"{payment} EUR",
                'date': get_current_date()
            }
            transactions.append(transaction_entry)

            new_bank_account = {
                'id': bank_account[-1]['id'] + 1,
                'tax_id': new_tax_id,
                'IBAN': generate_iban(),
                'balance': payment,
                'opening_date': get_current_date(),
                'bank': bank,
                'currency': currency,
                'transactions': transactions
                }
            
            bank_account.append(new_bank_account)

            print(f'You have paid the amount of {payment} EUR on your bank account!')
            print()
            print('You have successfully opened a bank account.')
            #test
            #for test in transactions:
                #print(test)
            print()
            print('In menu select option 2 for managing your account!')
            time.sleep(5)
            return main_menu()
            




def existing_account():
    clear_display()
    while True:
        found_company = None
        tax_id = input('Enter tax id of your company: ')

        for tax in company:
            if tax['tax_id'] == tax_id:
                found_company = tax
                break
        if found_company is not None:
            print('Company found:', found_company['name'])
            print()
            return bank_transactions()
        else:
            print('There is no company with that tax id. Please try again.')

        
#endregion

#region KEY FUNCTIONS
def main():
        menu_item = main_menu()

        if menu_item == 0:
            print()
            return
        
        elif menu_item == 1:
            opening_an_account()
            print()

        elif menu_item == 2:
            existing_account()
            print()

        else:
            print('Invalid number!!')
#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    main()
#endregion