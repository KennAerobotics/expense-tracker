# project + installment 5
# Author: Ken Michael I. Paguio
# Laboratory Activity 5 in Advanced Programming - Installment 5
print("=" * 40)
print("\t     EXPENSE TRACKER")
print("This is where the pollitians get their money.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100 and amount <= 200:
            print("  Big expense.")
        elif amount > 50 and amount <= 100:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        over_budget = budget < total
        left = budget - total
        tax_label = f"Tax ({tax_percent:.1f}%):"
        print(f"  {'Expenses:':<14}{count}")
        print(f"  {'Subtotal:':<14}${subtotal:.1f}")
        print(f"  {tax_label:<14}${tax:.1f}")
        print(f"  {'Grand total:':<14}${total:.1f}")
        if over_budget:
            print(f"  Over budget by ${-left:.1f}!")
        elif total > budget * 0.9:
            print(f"  Careful: only ${left:.1f} left.")
        else:
            print(f"  Within budget. ${left:.1f} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Ken Michael I. Paguio  |  Installment 5")
print("=" * 40)