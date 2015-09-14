# Alex W. Bishop
# alex.w.bishop@gmail.com
# RETURNS A LIST OF REAL WORD SUBSTRINGS IN A GIVEN STRING

def allRealWords(s, minLen):
    '''s: string
    minLen: int, min length of words (>= 2 letters). default: 2
    return: all real words >= minLen within s to a list'''
    import enchant
    engWord = enchant.Dict("en_US")
    StrLen = len(s) # length of s
    if minLen < 2:
        minLen = 2
    if StrLen < minLen: # exclude empty and single-char strings
        return []
    s = s.lower() # make lower case
    realWords = []
    nonRealWords = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(StrLen): # CHECK EACH CHAR AS THE s[0] OF A SUBSTRING
        if s[i] in alphabet: # any valid word must start with alpha
            j = i + minLen # START WITH minLen-LETTER WORDS
            while j <= StrLen: # CONTINUE SEARCHING UNTIL END OF S
                if s[j-1] in alphabet: # valid words contain alpha only
                    word = s[i:j] # WORD TO CHECK
                    if word not in realWords and word not in nonRealWords: # DON'T DOUBLE CHECK    
                        if engWord.check(word): # CHECK DICTIONARY
                            realWords.append(str(word)) # ADD VALID WORD TO LIST
                        else:
                            nonRealWords.append(str(word)) # KEEP TRACK OF CHECKED WORDS
                    j += 1 # MOVE TO NEXT CHAR
                else:
                    break # SKIP TO NEXT CHAR IN i
    realWords.sort()
    return realWords

s = str(raw_input('Enter raw text to check for real English words: '))
minLen = int(raw_input('Minimum word length (default: 2): '))
result = allRealWords(s, minLen)
print("Found %d valid words at least %d letters long: " % (len(result), minLen))
print(result)
