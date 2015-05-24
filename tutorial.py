# Useful keyboard shortcuts:
# ALT+P/N: Previous/next command


def add(x,y):
    print 'Add function returns: ' + str(x+y)
    return x+y

def printingLines():
    # Printing things of different types
    print str(123) + 'test'


def ifelseExample(str1,str2):
    print 'ifelseExample'
    if isinstance(str1,str):
        print 'str1 is actually a string!'
    else:
        print 'str1 is NOT a string =('

    if isinstance(str2,str):
        print 'str2 is also a string!'
    else:
        # Printing multiple line stuff
        print(""" Triple quotes can 'be' "used" to make """
            """sure any 'type" of any type of quote inside """
            """inside 'printed" text. """)

    printSeparator()
        
def whileExample(num):
    print 'whileExample(num)'
    if isinstance(num,int):
        while (num < 20):
            print num
            num = num+1

    printSeparator()

def usingStringsAndLists():
    print 'usingStringsAndLists():'
    # Defining a list
    list1 = ['C++','MATLAB','Python','Java','C#','random123','     ','2345']
    print list1
    # printing an element, finding the length, replace a character
    print list1[2],'+',len(list1),list1[0].replace('+','-'),list1[2].upper()
    # isalpha/isdigits/isspace: Checks if all chars in string is letters/numbers/spaces
    print list1[1].lower(), list1[7].isdigit(),list1[2].isalpha(),list1[6].isspace()
    # String finding for startswith or endswith, finding characters
    print ('Starts/Ends With: ',list1[1].startswith('MA') & list1[1].endswith('AB'),
           list1[2].find('o'),list1[2].find('k') )
    # If not found, find returns -1

    text = ("%d little pigs come out or I'll %s and %s and %s" %
    (3, 'huff', 'puff', 'blow down'))

    print ('Splitting up Java with "a" delimiter: %s.' % ', '.join(list1[3].split('a')))
    print list1[3].split('a')

    list2 = ['larry', 'curly', 'moe']
    list2.append('shemp')         ## append elem at end
    list2.insert(3, 'xxx')        ## insert elem at index 3
    list2.extend(['yyy', 'zzz'])  ## add list of elems at end
    print list2  ## ['larry', 'curly', 'moe', 'xxx', 'shemp', 'yyy', 'zzz']
    print list2.index('curly')    ## 2

    list2.remove('curly')         ## search and remove that element
    list2.pop(1)                  ## removes and returns 'moe' (pop goes from end)
    print list2  ## ['larry', 'xxx', 'shemp', 'yyy', 'zzz'] 

    numList = range(10)
    tot = 0;
    for num in numList:
        tot += num

    print numList

    printSeparator()
    

def sortingLists():

    print 'sortingLists()'
    list1 = ['C','az','ccc','DXEAW','12sd588'];
    # Sort alphabetically
    print sorted(list1) #['12sd588', 'C', 'DXEAW', 'az', 'ccc']
    # Sort by length of each string
    print sorted(list1,key=len) # ['C', 'az', 'ccc', 'DXEAW', '12sd588']
    # Sort by last character
    print sorted(list1,key=mySortingKey) # ['12sd588', 'C', 'DXEAW', 'ccc', 'az']
    
    list1.sort(key=mySortingKey) # Note that the sort() cmd doesn't RETURN anything!
    # list2 = list1.sort() will NOT work!
    print list1

    printSeparator()
    
        
def mySortingKey(str):
    # Return last character!
    return str[-1]
            
def TricksPart1():
    randStr = 'Hello world!'
    emptyStr = ''

    # Can just use "if" to check for empty strings
    if randStr:
        print 'Random string is NOT empty'
    else:
        print 'Random string is empty'
    
    if not emptyStr:
        print 'Empty string is empty!'

    printSeparator()

def printingPrettyLists():
    # List is strings inside square brackets. Fastest way to print strings,
    # Don't concatenate with for loop and +!
    print 'printingPrettyLists()'
    recent_presidents = ['George Bush', 'Bill Clinton', 'George W. Bush']
    print ('The three most recent presidents were: '
           '%s.' % ', '.join(recent_presidents) )

    printSeparator()

def printSeparator():
    print 
    print '%%%%%%%%%%%%%%%%%%%%%%'
    print 
          
def main():
    add(2,3)
    printingLines()
    ifelseExample('test1',3)
    whileExample(13)
    TricksPart1()
    printingPrettyLists()
    usingStringsAndLists()
    sortingLists()

	
if __name__ == "__main__":
    print __name__
    main()

