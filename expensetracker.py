#START

#Ask the user for their name
from random import choice


name = input("What is your name? ")

#Ask the user how much money they have
money = float(input("How much money do you have? "))

#Create a place to store expenses
expenses = []

#Show the menu
print("What would you like to do?")
print("1. Add Expense")
print("2. View Expenses")
print("3. View Total")
print("4. View Balance")
print("5. Exit")

#IF the user chooses Add Expense:
if choice == "1":
    #Ask for expense name
    expense_name = input("What is the expense name? ")
    #Ask for expense amount
    expense_amount = float(input("What is the expense amount? "))
    #Save the expense
    expenses.append((expense_name, expense_amount))
    #Show success message
    print("Expense added successfully!")

#IF the user chooses View Expenses:

    #Show all saved expenses

#IF the user chooses View Total:
    #Calculate all expenses
    #Show total

#IF the user chooses View Balance:
    #Calculate remaining money
    #Show balance

#IF the user chooses Exit:
    #End the program

#Otherwise:
    #Tell the user the option is invalid
#
#END