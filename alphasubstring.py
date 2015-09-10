# Alex W. Bishop
# alex.w.bishop@gmail.com
# RETURNS THE LONGEST ALPHABETICAL SUBSTRING OF A GIVEN STRING
s = str(raw_input('Enter a string: '))

def isAlphabetic(c1, c2):
    '''c1 and c2: one lowercase letter
       returns: True if c1 is in alphabetical order with c2, False otherwise.'''
    if c1 <= c2:
        return True
    else:
        return False

def AlphaSubStr(s):
    '''s = string of > 0 lower case alpha chars
    returns longest alphabetical substring in a given string
    if a tie, keeps the one that occured first'''
    # INITIAL PARAMETERS ASSUME INPUT IS AT LEAST ONE LOWERCASE ALPHA CHAR
    StrLen = len(s)     # length of input string s
    LongAlphaStr = s[0] # longest alphabetical substring of s
    LongAlphaStrLen = 1 # length of longest alphabetical substring of s
    
    for i in range(0, StrLen-1): # CHECK EACH CHAR FOR THE s[0] OF AN ALPHA SUBSTRING
        if len(s[i:]) > LongAlphaStrLen: # IF REMAINDER OF STRING COULD HOLD A LONGER ALPHA SUBSTRING
            j = i + 1 # set j to be the next char after i
            while j < StrLen: # CONTINUE SEARCHING UNTIL END OF INPUT STRING
                if isAlphabetic(s[j-1], s[j]) == True: # if these two chars are alphabetical
                    j += 1  # check the next char in the string
                else:
                    break # end of alpha substring reached
            # CHECK ALPHA SUBSTRING WITH LENGTH OF CURRENT RECORD
            if (len(s[i:j]) > LongAlphaStrLen): # if alpha substring found is longer than longest alpha string
                LongAlphaStr = s[i:j]  # set new longest alpha string
                LongAlphaStrLen = len(LongAlphaStr) # set new length to beat
    print("Longest substring in alphabetical order is: %s" % LongAlphaStr) # PRINT FINAL ANSWER

AlphaSubStr(s)
