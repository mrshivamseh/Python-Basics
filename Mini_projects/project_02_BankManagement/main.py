from bank import create_account, view_accounts, deposit_money, withdraw_money, check_single_balance, is_valid_account, verify_pin

while True:
    print("\n===== Bank Account Management System =====")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        try:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Opening Balance: "))
            pin = input("Set 4-Digit Secret PIN: ").strip()
            
            if len(pin) != 4 or not pin.isdigit():
                print("❌ Error: PIN must be exactly 4 digits!")
                continue
                
            create_account(name, balance, pin)
            print("Account created successfully!")
        except ValueError:
            print("❌ Balance must be a number!")
            
    elif choice == "2":
        view_accounts()
        
    elif choice == "3":
        try:
            account_id = int(input("Enter Account ID: "))
            if is_valid_account(account_id):
                entered_pin = input("Enter your 4-Digit PIN: ").strip()
                if verify_pin(account_id, entered_pin):
                    amount = float(input("Enter Amount to Deposit: "))
                    deposit_money(account_id, amount)
                else:
                    print("❌ Wrong PIN! Access Denied.")
            else:
                print(f"❌ Invalid Account ID! Account ID {account_id} does not exist.")
        except ValueError:
            print("❌ Invalid Input! Please enter numbers only.")
            
    elif choice == "4":
        try:
            account_id = int(input("Enter Account ID: "))
            if is_valid_account(account_id):
                entered_pin = input("Enter your 4-Digit PIN: ").strip()
                if verify_pin(account_id, entered_pin):
                    amount = float(input("Enter Amount to Withdraw: "))
                    withdraw_money(account_id, amount)
                else:
                    print("❌ Wrong PIN! Access Denied.")
            else:
                print(f"❌ Invalid Account ID! Account ID {account_id} does not exist.")
        except ValueError:
            print("❌ Invalid Input!")
            
    elif choice == "5":
        try:
            account_id = int(input("Enter Account ID: "))
            if is_valid_account(account_id):
                entered_pin = input("Enter your 4-Digit PIN: ").strip()
                if verify_pin(account_id, entered_pin):
                    check_single_balance(account_id)
                else:
                    print("❌ Wrong PIN! Access Denied.")
            else:
                print(f"❌ Invalid Account ID! Account ID {account_id} does not exist.")
        except ValueError:
            print("❌ Invalid Input!")
            
    elif choice == "6":
        print("Thank you for using our banking services!")
        break
        
    else:
        print("Invalid choice! Please select between 1-6.")
