#region Imports
import os
import time
import random
from datetime import date
#endregion

#region Data
companies = [
    {
        'id': 1,
        'name': 'ABC Software Ltd.',
        'tax_id': '01234567890',
        'hq': {
            'street': 'Duga ulica 15',
            'postal_code': '10290',
            'city': 'Zapresic',
            'country': 'Croatia'
        },
        'email': 'info@abc-software.hr'
    }
]

bank = {
    'id': 1,
    'name': 'Lipa po lipa Bank',
    'hq': {
        'street': 'Kratka ulica 5',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Croatia'
    }
}

currency = {
    'id': 1,
    'name': 'Euro',
    'symbol': '€',
    'code': 'EUR'
}

transactions = []
accounts = [
    {
        'id': 1,
        'tax_id': '01234567890',
        'IBAN': 'HR45875465481354654',
        'balance': 0.00,
        'opening_date': '2025-09-29',
        'bank': bank,
        'currency': currency
    }
]
#endregion

#region Utils
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_date():
    return date.today().strftime("%d-%m-%Y")

def generate_iban():
    return "HR" + ''.join(str(random.randint(0, 9)) for _ in range(19))
#endregion

#region Menus
def main_menu():
    while True:
        clear()
        print("== BANK MANAGER ==")
        print("1. OPEN ACCOUNT")
        print("2. I HAVE AN ACCOUNT")
        print("0. EXIT")
        choice = input("Choose an option: ")
        if choice in ['0', '1', '2']:
            return choice

def show_account(acc):
    print()
    print('-' * 30)
    print("IBAN:", acc['IBAN'])
    print("Balance:", acc['balance'], currency['symbol'])
    print("Currency:", currency['name'], f"({currency['code']})")
    print("-" * 30)

def show_transactions(tax_id):
    found = False
    for t in transactions:
        if t['tax_id'] == tax_id:
            print()
            print("-" * 30)
            print("IBAN:", t['IBAN'])
            print("Amount:", t['amount'])
            print("Date:", t['date'])
            print("-" * 30)
            found = True
    if not found:
        print("No transactions.")

def deposit(acc):
    print("== DEPOSIT ==")
    print()
    amount = input("Enter deposit amount: ")
    if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
        amount = float(amount)
        acc['balance'] += amount
        transactions.append({
            'tax_id': acc['tax_id'],
            'IBAN': acc['IBAN'],
            'amount': f"{amount} EUR",
            'date': get_date()
        })
        print()
        print("Deposit successful.")
    else:
        print("Invalid amount.")

def withdraw(acc):
    print("== WITHDRAWAL ==")
    print()
    amount = input("Enter withdrawal amount: ")
    if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
        amount = float(amount)
        if amount > acc['balance']:
            print("Insufficient funds.")
        else:
            acc['balance'] -= amount
            transactions.append({
                'tax_id': acc['tax_id'],
                'IBAN': acc['IBAN'],
                'amount': f"-{amount} EUR",
                'date': get_date()
            })
            print()
            print("Withdrawal successful.")
    else:
        print("Invalid amount.")

def owner_info(acc):
    for c in companies:
        if c['tax_id'] == acc['tax_id']:
            print()
            print('-' * 30)
            print("Name:", c['name'])
            print("Tax ID:", c['tax_id'])
            print("Email:", c['email'])
            print("Streat:", c['hq']['street']),
            print('Postal code:', c['hq']['postal_code']),
            print('City:', c['hq']['city']), 
            print('Country:', c['hq']['country'])
            print('-' * 30)
            print()
            return
    print("No owner data found.")

def account_menu(acc):
    while True:
        clear()
        print("1. Show account")
        print("2. Show transactions")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Owner info")
        print("0. Back")
        option = input("Choose an option: ")
        if option == '1':
            show_account(acc)
            input("Press ENTER to continue")
        elif option == '2':
            show_transactions(acc['tax_id'])
            input("Press ENTER to continue")
        elif option == '3':
            deposit(acc)
            input("Press ENTER to continue")
        elif option == '4':
            withdraw(acc)
            input("Press ENTER to continue")
        elif option == '5':
            owner_info(acc)
            input("Press ENTER to continue")
        elif option == '0':
            break
#endregion

#region Account Actions
def open_account():
    clear()
    print("== OPEN ACCOUNT ==")
    name = input("Company name: ")
    tax_id = input("Tax ID: ")
    email = input("Email: ")
    street = input("Street: ")
    postal_code = input("Postal code: ")
    city = input("City: ")
    country = input("Country: ")
    companies.append({
        'id': companies[-1]['id'] + 1,
        'name': name,
        'tax_id': tax_id,
        'hq': {
            'street': street,
            'postal_code': postal_code,
            'city': city,
            'country': country
        },
        'email': email
    })
    print("Minimum deposit is 500 EUR.")
    deposit_amount = input("Enter deposit amount: ")
    while not (deposit_amount.replace('.', '', 1).isdigit() and float(deposit_amount) >= 500):
        print("Minimum amount is 500 EUR.")
        deposit_amount = input("Enter deposit amount: ")
    deposit_amount = float(deposit_amount)
    iban = generate_iban()
    accounts.append({
        'id': accounts[-1]['id'] + 1,
        'tax_id': tax_id,
        'IBAN': iban,
        'balance': deposit_amount,
        'opening_date': get_date(),
        'bank': bank,
        'currency': currency
    })
    transactions.append({
        'tax_id': tax_id,
        'IBAN': iban,
        'amount': f"{deposit_amount} EUR",
        'date': get_date()
    })
    print("Account opened! IBAN:", iban)
    time.sleep(2)

def have_account():
    clear()
    tax_id = input("Enter company Tax ID: ")
    for acc in accounts:
        if acc['tax_id'] == tax_id:
            account_menu(acc)
            return
    print("Account not found.")
    input("Press ENTER to continue")
#endregion

#region Main
def main():
    while True:
        choice = main_menu()
        if choice == '0':
            break
        elif choice == '1':
            open_account()
        elif choice == '2':
            have_account()

if __name__ == '__main__':
    main()
#endregion
