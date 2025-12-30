from fun_tracker import *
print("--------PERSONAL EXPENSE TRACKER BY MAHESH-----------")

def main():
    initialize_file()
    while True:
        print(" 1.Add Expense\n 2.View Expense\n 3.Filter Expense\n 4.Delete Expense\n 5.Monthly Summary\n 6.Exit ")
        print("Enter your choice ")
        choice = int(input(":"))
        if choice == 1:
            date=input("Enter the date(YYYY-MM-DD): ")
            amount=float(input("Enter the amount: "))
            category=input("Enter the category: ")
            description=input("Enter the description: ")
            add_expense(date,amount,category,description)
            print()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            filter_by=input("Filter by (date/category) : ")
            filter_value=input(f"enter {filter_by}: ")
            filter_expense(filter_by,filter_value)
            print()
        elif choice == 4:
            date = input("Enter the date(YYYY-MM-DD): ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            delete_expense(date,amount,category,description)
            print()
        elif choice == 5:
            monthly_summary()
        elif choice == 6:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

if __name__ == '__main__':
    main()

