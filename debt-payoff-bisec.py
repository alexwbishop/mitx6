# Alex W. Bishop
# alex.w.bishop@gmail.com
# computes a fixed monthly payment to pay off an interest-bearing debt within x months
# uses bisection search
balance = float(raw_input("balance = ")) # starting balance to pay off
annualInterestRate = float(raw_input("annual interest rate = ")) # 0 < .2float < 1
period = int(raw_input("months to pay off by = ")) # int >= 1
precision = float(raw_input("monthly payment to be a multiple of = ")) # int or float
monthlyInterestRate = annualInterestRate/12.0

def endBalance(monthlyPmt, balance):
    '''RETURNS ENDING BALANCE AFTER PERIOD WITH A GIVEN FIXED MONTHLY PAYMENT
    monthlyPmt: int or .2float
    balance: int or .2float'''
    for month in range(int(period)):
        # ub = b - p
        unpaidBal = balance - monthlyPmt
        # b = ub + r/12 * ub
        balance = unpaidBal + monthlyInterestRate * unpaidBal
    return balance

def monthlyPmtPayoff(balance, annualInterestRate, period, precision): 
    '''RETURNS FIXED MONTHLY PAYMENT TO PAY OFF BALANCE WITHIN PERIOD
    balance: .2float, balance to pay off
    annualInterestRate: 0 < .2float < 1
    period: int (# of months to reduce balance to 0)
    precision = int or .2float, precision of monthlyPmt result'''
    monthlyPmtMin = balance/period # LOWER BOUND OF SEARCH
    monthlyPmtMax = (balance * (1 + monthlyInterestRate)**period) / period # UPPER BOUND OF SEARCH
    monthlyPmt = (monthlyPmtMax + monthlyPmtMin)/2.0  # SET MIDPOINT
    while abs(endBalance(monthlyPmt, balance)) > precision: # ANSWER TOO IMPRECISE
        if endBalance(monthlyPmt, balance) > 0: # TOO LOW, RAISE LOWER BOUND
            monthlyPmtMin = monthlyPmt
        else:                                   # TOO HIGH, REDUCE UPPER BOUND
            monthlyPmtMax = monthlyPmt
        monthlyPmt = (monthlyPmtMax + monthlyPmtMin)/2.0  # SET NEW MIDPOINT
    return monthlyPmt

# PRINT RESULT
print "Lowest Payment: %.2f" % monthlyPmtPayoff(balance, annualInterestRate, period, precision)
