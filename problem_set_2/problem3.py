balance = 320000
annualInterestRate = 0.2




def minn(x):
    min_monthlyPayment = round(x / 12, 2)
    return min_monthlyPayment

print(minn(320000))


def maxx(y):
    m = 1
    debt_after_year = y
    while m <= 12:
        debt_after_year = round(annualInterestRate / 12, 2) * debt_after_year + debt_after_year
        m += 1
    max_monthlyPayment = round(debt_after_year / 12, 2)
    return max_monthlyPayment

print(maxx(320000))

def lowest_payment(z):
    debt_after_year = z
    min = minn(z)
    max = maxx(z)
    while debt_after_year > 0 or debt_after_year < - 2:
        debt_after_year = z
        m = 1
        month_payment = round(min + (max - min) / 2, 2)
        while m <= 12:
            debt_after_year = debt_after_year - month_payment
            debt_after_year = annualInterestRate / 12 * debt_after_year + debt_after_year
            m +=1
        if debt_after_year > 0:
            min = month_payment
            max = max
        else:
            min = min
            max = month_payment
    month_payment = round(month_payment, 2)
    return month_payment

"""
month_payment = min(balance) + (max(balance) - min(balance)) / 2
print(month_payment)

debt_after_year = 3329
month_payment = 292.64
m = 1
while m <= 12:
    debt_after_year = debt_after_year - month_payment
    debt_after_year = annualInterestRate / 12 * debt_after_year + debt_after_year
    m += 1

print(debt_after_year)
"""

print(lowest_payment(balance))

