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
