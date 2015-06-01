__author__ = 'goldenxradian'
import re



def regexp():

    # Tutorial from: https://developers.google.com/edu/python/regular-expressions
    # re.search(pattern, string)

    str = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w', str)

    if match:
        print 'found', match.group()
    else:
        print 'No match found'

    # General definitions
    # Any character: a,X,9
    # These characters have special meanings. Must have backslash before them so that they work as expected: ^ $ * + ? { [ ] \ | ( )
    pigWithThreeEyes = 'piiig'
    pigWithNoEyes = 'p123gs@@'
    match = re.search('iii', pigWithThreeEyes)          #iii
    match = re.search('igs',pigWithThreeEyes)           # match == "None"; bool is false
    match = re.search(r'..g',pigWithThreeEyes)          # match.group() == "iig", "." is wildcard anything (except newline, \n)
    match = re.search(r'\d\d\d',pigWithNoEyes)          # match.group() == "123", "/d" is wildcard digit [0-9]
    match = re.search(r'\w\w',pigWithNoEyes)            # == "p1", "\w" is wildcard [A-Za-z0-9_]

    # Repetition: Add "+" and "*" to specify repetition in a patter
    # + = 1 or more occurrences to its left
    # * = 0 or more occurrences to its left; Both + and * try to find the leftmost/best match in the string
    # ? = 0 or 1 occurrences of the pattern to its left

    match = re.search(r'pi+', pigWithThreeEyes)         #since i+, multiple i's are matched (at least one)
    match = re.search(r'i+', (pigWithThreeEyes + 'iiiii'))   # Matches the first group with multiple i's

    ## \s* = zero or more whitespace chars
    ## Here look for 3 digits, optional separation by whitespace since using *
    match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')   #match.group() == "1 2   3"
    match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')     #match.group() == "12  3"
    match = re.search(r'\d\s*\d\s*\d', 'xx123xx')       #match.group() == "123"

    # ^ means start searching at the BEGINNING of the string
    match = re.search(r'^i\w+', pigWithThreeEyes)       #match == None because the string does not start with "i"
    match = re.search(r'i\w+', pigWithThreeEyes)        #match.group() == iiig, 1+ wildcard characters

    # Matching emails
    email = "purple random alice-b@google.com monkey dishwasher"
    match = re.search(r'\w+@\w+', email)                # match = "b@google. Not a full match because /w doesn't include "-" or "."

    # Square brackets: used to indicate a set of chars [abc] matches 'a','b' or 'c'.
    # All the backslash codes also work. "." does not work. Easy way to add on other "accepted" characters
    # Note that the +/* goes OUTSIDE the brackets
    match = re.search(r'[\w-]+@[\w.]+', email)          # First [] bracket: \w and "-" are accepted. Next [] bracket: \w and "." are accepted

    # Note that if you put parenthesis around the [] brackets, you can actually create groups.
    print match.group()

    match = re.search('([\w.-]+)@([\w.-]+)', email)
    if match:
        print "\n match = re.search('([\w.-]+)@([\w.-]+)', purple alice-b@google.com monkey dishwasher):"
        print match.group()   ## 'alice-b@google.com' (the whole match)
        print match.group(1)  ## 'alice-b' (the username, group 1)
        print match.group(2)  ## 'google.com' (the host, group 2)

    # What if you have MULTIPLE emails in a string? Use "FINDALL"
    str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

    ## Here re.findall() returns a list of all the found email strings
    emails = re.findall(r'[\w-]+@[\w.]+', str)  ## ['alice@google.com', 'bob@abc.com']
    print "\n\tSearch string: " + str
    for email in emails:
        # do something with each found email string
        print email

    # Can incorporate into csvread files
    # f = open(test.txt','r')
    # str = re.findall(r'SomePattern', f.read())

    #findall can also be used with the parenthesis to return multiple lists. Technically, you don't actually get the "@" returned if you do things this way.
    tuples = re.findall(r'([\w-]+)@([\w.]+)', str)
    # Can access things in the tuple by tuples[0][1]
    print tuples

    for tuple in tuples:
        print tuple[0]
        print tuple[1]

    # Can also have exceptions used at the end
    # re.IGNORECASE = ignores case
    # re.DOTALL = "." matches "newline" as well, which CAN mess you up since ".*" matches EVERYTHING until the end of a line
        # Techncially, \s (whitespace) matches newlines, so if you want to match a bunch of whitespace + newlines, can use \s*
    # re.MULTILINE: Within a string of multiple lines, allow "^" and "$" to match the start/end of each line (since ^/$ only matches the start and end of the entire string
    withUpperCase = "piiIiig"
    match = re.search(r'i+\w+', withUpperCase, re.IGNORECASE)

    print match.group()

def regexp2():

    # http://www.thegeekstuff.com/2014/07/python-regex-examples/
    contact = "Doe, John: 555-1212 \n Roe, Rohn: 123-2345"
    match = re.search(r'\w+, \w+: \d+-\d+', contact) # multiple letters, look for a comma and space, multiple letters, look for colon and space, any digits, dash, any digits
    print match.group()
    # Can also use grouping. Note the square brackets increases the search parameters to any digits AND dash.
    # Note the + goes ont he OUTSIDE of the square brackets!
    matches = re.findall(r'(\w+), (\w+): ([\d-]+)', contact)

    # Also note the output of findall is NOT in "match.group()" but is a tuple itself
    for tuple in matches:
        for item in tuple:
            print item


    # In case you want to match the LAST digits
    match = re.search(r'[\d-]+$', contact)
    print "Last match: ", match.group()
    match = re.search(r'^[\d-]+', contact)
    print "First/beginning of sentence match failed becasue the beginning of the string isn't actually any digit."

    # You can also NAME your matches! This way, the groups makes more sense. P = pattern name I guess.
    match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<num>[\d-]+)', contact)
    # That way, code becomes much more readable. I actually like this.
    print "match.group('last'): ", match.group('last')
    print "match.group('first'): ", match.group('first')
    print "match.group('num'): ", match.group('num')

    str = "This is a full sentence"
    matches = re.findall(r'\w+', str)       # Now each word is separated into it's item in a list.
    print matches

def main():
    regexp()
    regexp2()

if __name__ == "__main__":
    main()