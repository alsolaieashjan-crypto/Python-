Exit = False
option = 0

nisab = 0
gold_nisab = 85
silver_nisab = 595


def get_option(print_menu):
    if print_menu:
        print("Enter the number of the option you want to select:")
        print("1. Calculate the Zakat")
        print("2. Edit the Nisab")
        print("3. Exit")
        return int(input())
    else:
        return int(input("Enter the number of the option you want, or 0 to redisplay the menu\n"))


def get_total_balance():
    num_accounts = int(input("How many bank accounts do you have? "))
    total_balance = 0
    for i in range(1, num_accounts + 1):
        balance = int(input(f"Enter balance for bank account {i}: "))
        total_balance += balance
    return total_balance


def compute_zakat(nisab):
    total_balance = get_total_balance()

    zakat = round(0.025 * total_balance, 3)

    if total_balance < nisab:
        zakat = 0.0

    print("\nOutput: Given a nisab of:", nisab,
          "and with a total balance of", total_balance,
          "your zakat is :", zakat, "SR \n")


def compute_nisab():
    global nisab

    print("Enter the Nisab measuring metal ('Silver', 'Gold', or 'Both' for the cheapest of silver and gold)")
    metal = input().lower()

    if metal in ["gold", "g"]:
        price = int(input("Enter the price of 1g of gold: "))
        nisab = price * gold_nisab

    elif metal in ["silver", "s"]:
        price = int(input("Enter the price of 1g of silver: "))
        nisab = price * silver_nisab

    elif metal in ["both", "b"]:
        gold_price = int(input("Enter price of 1g of pure gold: "))
        silver_price = int(input("Enter price of 1g of silver: "))
        nisab = min(gold_price * gold_nisab, silver_price * silver_nisab)

    nisab = round(nisab, 3)
    print("\nOutput: The nisab is", nisab, " SR \n")


def terminate_program():
    global Exit
    Exit = True
    print("\nOutput: Thank you for using our system. Exiting now")


while not Exit:

    if option == 0:
        option = get_option(True)

    elif option == 1:
        compute_zakat(nisab)
        option = get_option(False)


    elif option == 3:
        terminate_program()

    else:
        print("\nOutput: Invalid menu option. please enter an integer number from the menu.")
        option = 0
        
