# Alex W. Bishop
# alex.w.bishop@gmail.com
def PayMinimum(balance, annualInterestRate, monthlyPaymentRate, period):
    '''calculates debt balance after x months if only paying the minimum monthly payment required
    balance: .2float
    annualInterestRate = .2float
    monthlyPaymentRate = .2float
    period: int (# of months to pay minimum)'''
    totalPaid = 0.0
    # PRINT BALANCE AT END OF EACH MONTH
    for month in range(int(period)):
        print "Month: %d" % (month + 1)
        # ub = b - p
        monthlyPmt = monthlyPaymentRate * balance
        totalPaid += monthlyPmt
        print "Minimum monthly payment: %.2f" % monthlyPmt
        unpaidBal = balance - monthlyPmt
        # b = ub + r/12 * ub
        monthlyInterestRate = annualInterestRate/period
        balance = unpaidBal + monthlyInterestRate * unpaidBal
        print "Remaining balance: %.2f" % balance
    # PRINT FINAL PAID AND REMAINING BALANCE
    print "Total paid: %.2f" % totalPaid
    print "Balance after %d months: %.2f" % (period, balance)

# PROMPT FOR INPUTS
balance = float(raw_input("balance = ")) # current balance at beginning of year
annualInterestRate = float(raw_input("annual interest rate = ")) # > 0, < 1
monthlyPaymentRate = float(raw_input("monthly payment rate = ")) # > 0, < 1
period = int(raw_input("months to pay minimum for = ")) # >= 1

# COMPUTE & PRINT RESULTS
PayMinimum(balance, annualInterestRate, monthlyPaymentRate, period)
