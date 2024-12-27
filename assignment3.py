balance = 1000
print("ATM Name")

while True:
    print("Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        print(f"Check Balance: ${balance}")
    elif choice == "2":
        amount = float(input("Deposit Your Amount: $"))
        balance += amount
        print(f"Deposit Successful! Your new Balance: ${balance}")
    elif choice == "3":
        amount = float(input("Please Enter Your Withdraw Amount: $"))
        if amount <= balance:
            balance -= amount
            print(f"Withdraw Successful! New Balance: ${balance}")
        else:
            print("Insufficient balance")
    elif choice == "4":
        print("Thank you for using My ATM")
        break  # Exits the loop and the program
    else:
        print("Invalid Choice. Try again.")
