def dictionaryBasics():
    
    alphabetDict = dict(a=1,b=2,c=3,d=4)
    # OR
    # This requires more quotes haha.
    alphabetDict2 = {'a':1,'b':2,'c':3,'d':4}
    print alphabetDict
    
    # Turn dictionary into list
    alphabetList = alphabetDict2.items()
    print alphabetList
    
    # Creating the list manually
    l1 = ['a','b','c','d']
    l2 = [1,2,3,4]
    newList = zip(l1,l2) # Zip sort of "combines" the lists
    print len(newList)
    # dict can take at MOST length of 2 lists!
    list2dict = dict(newList)
    print list2dict
    printSeparator()
    
def dictionaryComprehensions():
    
    emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
    email_at_dotcom = dict( [name, '.com' in email] for name, email in emails.iteritems() )
    print "Dictionary of Emails: "
    print emails
    print email_at_dotcom
    # email_at_dotcom now is {'Dick': True, 'Jane': True, 'Stou': False}


def printSeparator():
    print 
    print '%%%%%%%%%%%%%%%%%%%%%%'
    print 
          
def main():
    
    dictionaryBasics()
    dictionaryComprehensions()

	
if __name__ == "__main__":
    print __name__
    main()
