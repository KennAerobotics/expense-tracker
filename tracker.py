# project + installment 3
# Author: Ken Michael I. Paguio
# Laboratory Activity 2 in Advanced Programming
subtotal = 0
print("=" * 40)
print("\t     EXPENSE TRACKER")
print("This is where the pollitians get their money.")
print("=" * 40)
print("\nMAIN MENU")
print("  [1] Add an expense\t\t(coming soon)")
print("  [2] View all expenses\t\t(coming soon)")
print("  [3] Show total spent\t\t(coming soon)")
print("  [4] Exit\t\t\t(coming soon)\n")
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n\n")
expense1 = str(input("First expense? "))
amount1 = float(input("Amount? "))
subtotal = amount1
expense2 = str(input("Second expense? "))
amount2 = float(input("Amount? "))
subtotal += amount2
average = (amount1 + amount2) / 2
tax_percent = int(input("Tax rate %? "))
budget = int(input("Your budget? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax
over_budget = budget < total
left = budget - total
print("")
print("-" * 40)
print("SUMMARY")
print(f"  -  {expense1}:\t   ${amount1:.1f}")
print(f"  -  {expense2}:\t   ${amount2:.1f}")
print(f"Subtotal:\t   ${subtotal:.1f}")
print(f"Average:\t   ${average:.2f}")
print(f"Tax ({tax_percent}%):\t   ${tax:.1f}")
print(f"Grand Total:\t   ${total:.1f}")
print(f"Over Budget?:\t   {over_budget}")
print(f"Left in Budget:\t   ${left:.1f}")
print("-" * 40)
print("Made by: Ken Michael I. Paguio | Installment 3")