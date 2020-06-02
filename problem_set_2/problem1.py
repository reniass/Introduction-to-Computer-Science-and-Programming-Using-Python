balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 1
while month <= 12:
    min_monthly_payment = monthlyPaymentRate * balance
    balance = balance - min_monthly_payment
    balance = balance + (annualInterestRate / 12) * balance
    balance  = round(balance, 2)
    month = month + 1



print(balance)