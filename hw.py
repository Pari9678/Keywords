def calculate_change(total_bill, amount_paid):
    change = amount_paid - total_bill
    return change

bill = 2.50
paid = 4.00

result = calculate_change(bill, paid)
print("Change to return:", result)