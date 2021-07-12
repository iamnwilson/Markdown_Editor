income = int(input())
if income <= 15527:
    tax = 0
elif income <= 15528 or income <= 42707:
    tax = 15
elif income <= 42708 or income <= 132406:
    tax = 25
elif income >= 132407:
    tax = 28
calculated_tax = int(round(income * tax / 100))
print(f'The tax for {income} is {tax}%. That is {calculated_tax} dollars!')
