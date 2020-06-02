for i in range(1, 13):
    minimum_monthly_payment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimum_monthly_payment
    balance = unpaidBalance + unpaidBalance * (annualInterestRate / 12)

balance = round(balance, 1)
print("Remaining balance: %d" % balance)
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

