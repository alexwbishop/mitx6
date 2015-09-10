# Alex W. Bishop
# alex.w.bishop@gmail.com
# guesses a secret number chosen by the user using bisection search
# number is only stored in human's head during guessing

def GuessTheNumber(low, high):
    '''low and high: int
    returns an int within low and high according to user response'''
    response = None
    print('Please think of a number between %d and %d!' % (low, high)) # prompts for secret number
    guess = (high + low)/2  # make initial midpoint guess
    while response != 'c':
        print('Is your secret number %d?' % guess) # ask user if guess is correct
        print "Enter 'h' to indicate the guess is too high. ",
        print "Enter 'l' to indicate the guess is too low. ",
        print "Enter 'c' to indicate I guessed correctly.",
        response = str(raw_input(''))
        if response == 'l':          
            low = guess         # too low, raise lower bound
        elif response == 'h':
            high = guess          # too high, reduce upper bound
        elif response == 'c':
            ans = guess             # guess corect, set guess to final answer
            break                   # exit guessing loop
        else:
            print "Sorry, I did not understand your input."
        guess = (high + low)/2  # guess midpoint between low and high range
    print('Game over. Your secret number was: %d!' % ans) # print game over

GuessTheNumber(0, 100)
