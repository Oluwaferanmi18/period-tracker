#START

#Ask the user for their name
name = input("What is your name? ")

#Ask the user how much money they have
money = float(input("How much money do you have? "))
print()

#Create a place to store expenses
expenses = []



while True:
    #Show the menu
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. View Balance")
    print("5. Exit")
    #Get the user's choice
    choice = input("Please select an option: ")

    #IF the user chooses Add Expense:
    if choice == "1":
        #Ask for expense name
        expense_name = input("What is the expense name? ")
        #Ask for expense amount
        expense_amount = float(input("What is the expense amount? "))
        print()
        #Save the expense
        expenses.append((expense_name, expense_amount))
        #Show success message
        print("Expense added successfully!")
        print()

    #IF the user chooses View Expenses:
    elif choice == "2":
        #Show all saved expenses
        print(expenses)
        print()

    #IF the user chooses View Total:
    elif choice == "3":
        #Calculate all expenses
        total = sum(amount for _, amount in expenses)
        #Show total
        print(f"Total expenses: {total}")
        print()

    #IF the user chooses View Balance:
    elif choice == "4":
        #Calculate remaining money
        balance = money - sum(amount for _, amount in expenses)
        #Show balance
        print(f"Remaining balance: {balance}")
        print()

    #IF the user chooses Exit:
    elif choice == "5":
        #End the program
        print("Thank you for using the expense tracker!")
        break

    #Otherwise:
    else:
        #Tell the user the option is invalid
        print("Invalid option. Please try again.")
        print()
    #
    #END