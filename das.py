import datetime

school_expenses = {
    "Tuition Fees": 15000,
    "Laboratory Fees": 5000,
    "Books fees": 2500,
    "Miscellaneous Fees": 2000,
    "School uniform set Fees": 5000
}

def main():
    while True:
        print("Welcome to the School Expense Management System wewewewww!")
        print("Please choose an option (murag ikaw pang option):")
        print("1. Add a new payment record")
        print("2. View all payment records")
        print("3. Exit")

        choice = input("Select a number from the options: ")

        if choice == "1":
            add_payment()
        elif choice == "2":
            read_expenses()
        elif choice == "3":
            print("Thank you for using our system! Have a great day ahead shoulder knees and toes!")
            break
        else:
            print("Erkk! That's not a valid option. Please choose again.")

file_name = "school_expenses.txt"

def calculate_total_fee():
    return sum(school_expenses.values())

def save_to_txt(payment_record):
    with open(file_name, 'a') as file:
        file.write(f"Student Name: {payment_record['student_name']}\n")
        file.write(f"Student ID: {payment_record['student_id']}\n")
        file.write(f"Expense: {payment_record['expense']}\n")
        file.write(f"Amount Paid: Php {payment_record['amount_paid']}\n")
        file.write(f"Remaining Balance: Php {payment_record['remaining_balance']}\n")
        file.write(f"Date Paid: {payment_record['date_paid']}\n")
        file.write("-----\n")

def load_data():
    try:
        with open(file_name, 'r') as file:
            data = file.read().splitlines()
    except FileNotFoundError:
        data = []
    return data

def read_expenses():
    data = load_data()
    if data:
        print("Here are the payment records we have so far:")
        for record in data:
            if record == "-----":
                print()
            else:
                print(record)
    else:
        print("No records found pa.")

def add_payment():
    student_name = input("Hi dzai! What's your name? ")
    student_id = input(f"Hello dai, {student_name}! Can you please provide your student ID? ")

    total_due = calculate_total_fee()
    total_paid = 0
    expenses_paid = []

    while True:
     
        print(f"\nPlease choose the number of the expense you paid, {student_name}:")
        expense_choices = list(school_expenses.keys())
        for index, expense in enumerate(expense_choices, start=1):
            print(f"{index}. {expense}")
        
        expense_choice = input("Enter the number of the expense: ")
        
        try:
            expense_choice = int(expense_choice)
            if expense_choice < 1 or expense_choice > len(expense_choices):
                print("Erkk invalid choice! Please enter a valid number.")
                continue
        except ValueError:
            print("Erkk invalid input! Please enter a number.")
            continue
        
        expense_selected = expense_choices[expense_choice - 1]
        expense_amount = school_expenses[expense_selected]
        
        if expense_selected in expenses_paid:
            print(f"You've already paid for {expense_selected}. Choose another expense.")
            continue
  
        try:
            amount_paid = float(input(f"How much have you paid for {expense_selected}? Php "))

            if amount_paid > expense_amount:
                print(f"Erkk!! You’ve entered an overpayment! The {expense_selected} amount is Php {expense_amount}.")
                print(f"Your payment nilabaw sa Php {amount_paid - expense_amount}.")
                amount_paid = float(input(f"Please enter a valid payment (maximum Php {expense_amount}): Php "))
                if amount_paid > expense_amount:
                    print(f"Erkkk! You cannot pay more than the amount due for {expense_selected}. The total for this expense is Php {expense_amount}.")
                    continue
            else:
                pass
            
        except ValueError:
            print("Erkk! Please enter a valid number for the payment.")
            continue

        expenses_paid.append(expense_selected)
        total_paid += amount_paid
        
        date_paid = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
        payment_record = {
            "student_name": student_name,
            "student_id": student_id,
            "expense": expense_selected,
            "amount_paid": amount_paid,
            "remaining_balance": total_due - total_paid,
            "date_paid": date_paid
        }

        save_to_txt(payment_record)

        more_expenses = input("Are there any other expenses from the choices you have already paid? (yes/no): ").lower()
        if more_expenses != 'yes':
            break

    print("\nHere’s a breakdown of your school expenses:")
    for expense, amount in school_expenses.items():
        print(f"- {expense}: Php {amount}")
    print(f"\nTotal Amount Due: Php {total_due}")
    print(f"Total Amount Paid: Php {total_paid}")
    print(f"Final Remaining Balance: Php {total_due - total_paid}")

if __name__ == "__main__":
    main()










