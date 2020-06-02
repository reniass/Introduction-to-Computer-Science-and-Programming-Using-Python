
balance = 3329
annualInterestRate = 0.2

monthlyPayment = 0
new_balance = 100
while new_balance >= 0:
    new_balance = balance
    monthlyPayment = monthlyPayment + 10
    m = 0
    while m < 12:
        m = m + 1
        new_balance = new_balance - monthlyPayment
        new_balance = annualInterestRate / 12 * new_balance + new_balance
#    print(balance)



print(monthlyPayment)

"""
new_balance = 3329
annualInterestRate = 0.2
monthlyPayment = 310
m = 0
while m < 12:
    m = m + 1
    new_balance = new_balance - monthlyPayment
    new_balance = annualInterestRate / 12 * new_balance + new_balance
    print(m, new_balance)
"""