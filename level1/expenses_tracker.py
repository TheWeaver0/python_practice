def add_expenses(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def list_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']} \n")

def total_expenses(expenses):
    return sum(map(lambda expense:expense['amount'], expenses))

def filtering_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'] == category, expenses))


def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses ')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit\n')
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expenses(expenses, amount, category)
        elif choice == '2':
            print('\nAll expenses:\n')
            list_expenses(expenses)
        elif choice == '3':
            print(f'\nTotal expenses: {total_expenses(expenses)}')
        elif choice == '4':
            category = input('Enter category: ')
            print('\nFiltered list: \n')
            list_expenses(filtering_by_category(expenses, category))
        elif choice == '5':
            print('Exiting the program.')
            break
main()