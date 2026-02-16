TEAM X
def calculate_total_bill(amount, tip_percent):
    amount = float(amount)
    tip_percent = float(tip_percent)
    tip_amount = amount * (tip_percent / 100)
    Total = amount + tip_amount
    return Total
amount = input()
tip_percent = input()
total_bill = calculate_total_bill(amount, tip_percent)
print(f"{total_bill:.2f}")
