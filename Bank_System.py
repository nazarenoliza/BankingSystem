accounts = {}
balances = {}

def register():
    
    acc_num = input("Enter account number: ")

    if acc_num in accounts:
        print("Account already exists!")
        return

    pin = input("Enter PIN: ")
    accounts[acc_num] = pin
    balances[acc_num] = 0.0  
    print("Account successfully registered.")

def login():
    
    acc_num = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if acc_num in accounts and accounts[acc_num] == pin:
        print("Login successful!")
        account_menu(acc_num) 
    else:
        print("Invalid account number or PIN.")

def account_menu(acc_num):
    
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        
        choice = input("Enter choice: ")

        if choice == "1":
            check_balance(acc_num)
        elif choice == "2":
            deposit(acc_num)
        elif choice == "3":
            withdraw(acc_num)
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

def check_balance(acc_num):
   
    print(f"Current balance: ${balances[acc_num]:.2f}")

def deposit(acc_num):
    
    try:
        amount = float(input("Enter amount to deposit: "))
        
        if amount > 0:
            balances[acc_num] += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount! Please enter a positive value.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def withdraw(acc_num):
    
    try:
        amount = float(input("Enter amount to withdraw: "))
        
        if 0 < amount <= balances[acc_num]:
            balances[acc_num] -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount!")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def main():
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "_main_":
    main()