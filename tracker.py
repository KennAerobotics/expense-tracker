# project + installment 2
# Author: Ken Michael I. Paguio
# Laboratory Activity 2 in Advanced Programming

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
expense2 = str(input("Second expense? "))
amount2 = float(input("Amount? "))
average = (amount1 + amount2) / 2
print("")
print("-" * 40)
print("SUMMARY")
print(f"  -  {expense1}:\t   ${amount1:.1f}")
print(f"  -  {expense2}:\t   ${amount2:.1f}")
print(f"Total spent:\t   ${amount1 + amount2:.1f}")
print(f"Average:\t   ${average:.2f}")
print("-" * 40)
print("Made by: Ken Michael I. Paguio | Installment 2")