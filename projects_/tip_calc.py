"""Tip Calculator
Input bill amount and tip percentage.
Calculate total bill.
Use round() to format the result."""

bill_ammount = float(input('Enter bill amount:'))
tip_perc = float(input('Enter tip percentage:'))

tip = float(bill_ammount * (tip_perc / 100))
total_bill = bill_ammount + tip


print("Bill amount: $", round(bill_ammount, 2))
print("Tip: $", round(tip, 2))
print("Total bill: $", round(total_bill, 2))