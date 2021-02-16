if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Problem 1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year if a person
# only pays the minimum monthly payment required by the credit card company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance.
# Be sure to print out no more than two decimal digits of accuracy - so print

def creditcard(balance, annualInterestRate, monthlyPaymentRate):
    '''calculates balance after one year if only minimum monthly payments are made.

    >>> c = creditcard(42, 0.2, 0.04)
    >>> print(c)
    Remaining balance: 31.38
    '''
    Interest_Per_Month = annualInterestRate / 12
    for _ in range(12):
        current_minimum_repayment = balance * monthlyPaymentRate
        Monthly_unpaid_balance = balance - current_minimum_repayment
        balance = Monthly_unpaid_balance + Interest_Per_Month * Monthly_unpaid_balance
    return "Remaining balance: {0}".format(round(balance, 2))

# Problem 2 - Paying Debt Off in a Year
#
# Now write a program that calculates the minimum fixed monthly payment needed in
# order pay off a credit card balance within 12 months. By a fixed monthly payment,
# we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year

def credit_card_repay(balance, annualInterestRate, monthlyPayment):
    if balance > monthlyPayment * 12:
        return 1
    Interest_Per_Month = annualInterestRate / 12
    for _ in range(12):
        Monthly_unpaid_balance = balance - monthlyPayment
        balance = Monthly_unpaid_balance + Interest_Per_Month * Monthly_unpaid_balance
    return balance

def monthly_repayment(balance, annualInterestRate, payment):

    a = credit_card_repay(balance, annualInterestRate, payment)
    if a <= 0:
        return "Lowest Payment: {0}".format(payment)
    else:
        monthly_repayment(balance, annualInterestRate, payment + 10)
# balnce and annualInterestRate given by checker
print(monthly_repayment(3329, 0.2, 10))

# Problem 3 - Using Bisection Search to Make the Program Faster
#
# In short:
#
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#
# Write a program that uses these bounds and bisection search
# to find the smallest monthly payment to the cent (no more multiples of $10)
# such that we can pay off the debt within a year.
# Try it out with large inputs, and notice how fast it is.
# Produce the same return value as you did in Problem 2.

def credit_card_bisection(balance, monthly_interest_rate, monthlyPayment):
    for _ in range(12):
        Monthly_unpaid_balance = balance - monthlyPayment
        balance = Monthly_unpaid_balance + monthly_interest_rate * Monthly_unpaid_balance
    return balance

def bisection_credit_card(balance, annualInterestRate):
    monthly_interest_rate = annualInterestRate / 12
    lower = balance / 12
    upper = balance * pow(1 + monthly_interest_rate, 12) / 12
    payment = (lower + upper) / 2
    prev = 0
    while round(payment, 2) != round(prev, 2):
        prev = payment
        a = credit_card_bisection(balance, monthly_interest_rate, payment)
        if a >= 0:
            lower = payment
        else:
            upper = payment
        payment = (lower + upper) / 2

    return "Lowest Payment: {0}".format(round(payment, 2))

print(bisection_credit_card(320000, 0.2))
print(bisection_credit_card(999999, 0.18))
