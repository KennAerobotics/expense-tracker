# project + installment 4
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

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal = amount1
expense2 = str(input("Second expense? "))
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

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
print(f"  -  {expense1}:\t${amount1:.1f}")
print(f"  -  {expense2}:\t${amount2:.1f}")
print(f"Subtotal:\t${subtotal:.1f}")
print(f"Average:\t${average:.2f}")
print(f"Tax ({tax_percent}.0%):\t${tax:.1f}")
print(f"Grand Total:\t${total:.1f}")

if over_budget:
    print(f"Over budget by ${-left:.1f}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left:.1f} left.")
else:
    print(f"Within budget. ${left:.1f} left.")

print("-" * 40)
print("Made by: Ken Michael I. Paguio | Installment 4")