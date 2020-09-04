# regular expression library
import re
"""
Basic Flags in REGEX are I,L,M,S,U,X:
    re.I - it's used for ignoring casing
    re.L - it's used to find a local dependent
    re.M - it's used to find patterns throughout multiple lines
    re.S - it's used to find dot matches
    re.U - it's used for unicode
    re.X - it's used for writing regex in a readable format

REGEX Functionalities:
    Regex: [ab]
        - it finds a single occurrence of character a and b.
    Regex [^ab]
        - it finds character except for a and b
    Regex [a-z]
        - it finds character range of a to z
    Regex [^a-z]
        - it finds a range except to z
    Regex [a-zA-Z]
        - it finds all the characters a to z as well as A to Z
    Regex []
        - it finds any single character
    Regex \s
        - any whitespace character
    Regex \S
        - any non-whitespace character
    Regex \d
        - any digit
    Regex \D
        - any non-digit
    Regex \W
        - any non-words
    Regex \w
        - any words
    Regex (a|b)
        - Either it matches a or b
    Regex a?;?
        - if it matches zero or one occurrence but not more than one occurence
    Regex a*;*
        - if it matches zero or more than one occurence
    Regex a+;+
        - if it matches one or more than one time
    Regex a{3}
        - if it matches three occurrence
    Regex a{3,}
        - if it matches simultaneous occurrences of a with 3 or more
    Regex a{3,6} 
        -if it matches simultaneous occurrences of a between 3 to 6
    Regex ^
        - starting of a string
    Regex $
        - Ending a string
    Regex \b
        - matches word boundary
    Regex \B
        - matches non-word boundary

    re.match()
        - it checks for a match of the string only at the beginning of the string. if it finds the pattern at the beginning of the input string, then it returns the matched pattern; otherwise it returns a noun.
    re.search()
        - it checks for a match of the string anywhere in the string and it finds all occurrence of the pattern in the given input string.

"""
# Tokenizing - Spliting sentences into word
# run the split query
re.split('\s+',"I like this book.")
# Extracting Email
doc = "For more details please mail us at: xyz@abc.com, pqr@mno.com"
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
for address in addresses:
    print(address)
# Replacing Emails
doc = "For more details please mail us at xyz@abc.com"
new_email = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'pqr@mno.com',doc)
new_email
