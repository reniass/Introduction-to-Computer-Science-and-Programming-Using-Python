"""
annualInterestRate = 0.2
balance = 420
monthlyInterestRate = annualInterestRate / 12


def monthlyPaymentLowerBound(balance):
    return balance / 12

def monthlyPaymentUpperBound(balance, monthlyInterestRate):
    return (balance * (1 + monthlyInterestRate)** 12) / 12

print(monthlyPaymentLowerBound(balance))
print(monthlyPaymentUpperBound(balance, monthlyInterestRate))


def lowestPayment(balance, monthlyInterestRate):
    copyBalance = balance
    while copyBalance > 0:
        copyBalance = balance
        monthlyPayment = monthlyPaymentLowerBound(balance) + (monthlyPaymentUpperBound(balance, monthlyInterestRate) - monthlyPaymentLowerBound(balance)) / 2
        for month in range(12):
            unpaidBalance = copyBalance - monthlyPayment
            copyBalance = unpaidBalance + unpaidBalance * monthlyInterestRate
        if copyBalance > 10:
"""
balance = 420
annualInterestRate = 0.2
monthlyInterestRate = round(annualInterestRate / 12, 2)




def lowestPayment(balance, annualInterestRate):
    copyBalance = balance
    monthlyInterestRate = round(annualInterestRate / 12, 2)
    minimum = balance / 12
    maximum = (balance * (1 + monthlyInterestRate) ** 12) / 12
    while copyBalance > 0:
        copyBalance = balance
        monthlyPayment = round(minimum + (maximum - minimum) / 2)
        for month in range(12):
            unpaidBalance = copyBalance - monthlyPayment
            copyBalance = unpaidBalance + unpaidBalance * (annualInterestRate / 12)
        if copyBalance > 10:
            minimum = monthlyPayment
            #maximum = maximum
        elif copyBalance < - 10:
            maximum = monthlyPayment
        else:
            return monthlyPayment

print(lowestPayment(420, 0.2))