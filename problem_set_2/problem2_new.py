annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
balance = 410
minimumFixedMonthlyPayment = 0
balanceCopy = balance

while balanceCopy > 10:
    balanceCopy = balance
    minimumFixedMonthlyPayment += 10
    for month in range(12):
        unPaidBalance = balanceCopy - minimumFixedMonthlyPayment
        balanceCopy = unPaidBalance + unPaidBalance * monthlyInterestRate


print(minimumFixedMonthlyPayment)


