import os

FILE_NAME = "account.txt"

def get_next_id():
    """Auto-generate incremental Account ID correctly"""
    if not os.path.exists(FILE_NAME):
        return 1
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return 1
        for line in reversed(lines):
            if line.strip():
                parts = line.strip().split(",")
                return int(parts[0]) + 1
    return 1

def create_account(name, balance, pin):
    """New account create karne ke liye"""
    account_id = get_next_id()
    with open(FILE_NAME, "a") as f:
        f.write(f"{account_id},{name},{balance},{pin}\n")
    print(f"\n✅ Account ID allocated: {account_id}")

def is_valid_account(account_id):
    """Account ID validation"""
    if not os.path.exists(FILE_NAME):
        return False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                if int(parts[0]) == account_id:
                    return True
    return False

def verify_pin(account_id, entered_pin):
    """PIN matching with strip feature"""
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                if int(parts[0]) == account_id:
                    # strip() se hidden newline character hat jata hai
                    return parts[3].strip() == str(entered_pin)
    return False

def view_accounts():
    """Admin function to see all accounts"""
    print("\n--- All Bank Accounts ---")
    if not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        print("No accounts found!")
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                print(f"ID: {parts[0]} | Name: {parts[1]} | Balance: ₹{float(parts[2]):.2f}")

def deposit_money(account_id, amount):
    """Money deposit logic"""
    if amount <= 0:
        print("❌ Amount must be greater than zero!")
        return
    updated_lines = []
    updated = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                if int(parts[0]) == account_id:
                    new_balance = float(parts[2]) + amount
                    updated_lines.append(f"{parts[0]},{parts[1]},{new_balance},{parts[3].strip()}\n")
                    updated = True
                    print(f"\n💰 ₹{amount:.2f} deposited successfully!")
                    print(f"💳 New Balance for ID {account_id}: ₹{new_balance:.2f}")
                else:
                    updated_lines.append(line)
    if updated:
        with open(FILE_NAME, "w") as f:
            f.writelines(updated_lines)

def withdraw_money(account_id, amount):
    """Money withdraw logic"""
    if amount <= 0:
        print("❌ Amount must be greater than zero!")
        return
    updated_lines = []
    updated = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                if int(parts[0]) == account_id:
                    current_balance = float(parts[2])
                    if amount > current_balance:
                        print(f"❌ Insufficient funds! Available Balance: ₹{current_balance:.2f}")
                        return
                    new_balance = current_balance - amount
                    updated_lines.append(f"{parts[0]},{parts[1]},{new_balance},{parts[3].strip()}\n")
                    updated = True
                    print(f"\n💸 ₹{amount:.2f} withdrawn successfully!")
                    print(f"💳 Remaining Balance for ID {account_id}: ₹{new_balance:.2f}")
                else:
                    updated_lines.append(line)
    if updated:
        with open(FILE_NAME, "w") as f:
            f.writelines(updated_lines)

def check_single_balance(account_id):
    """Single account balance check"""
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(",")
                if int(parts[0]) == account_id:
                    print(f"\n💳 Account ID: {parts[0]}")
                    print(f"👤 Holder Name: {parts[1]}")
                    print(f"💵 Net Balance: ₹{float(parts[2]):.2f}")
                    return
