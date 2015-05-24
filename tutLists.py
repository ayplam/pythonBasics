def listOfSquares():
    orig = [];
    square1 = [];
    
    # xrange is the same as get 10 elements starting from 0. help(xrange)
    for num in xrange(10):
        orig.append(num)
        
    # The n00b way of using append
    for num in orig:
        square1.append(num*num);

    print("Original: ")
    print orig
    print("Squares1: ")
    print square1
    
    # map accepts a function and a list, applying the function on all elements of the list
    square2 = map(lambda x:x*x,orig)
    print("Squares2: ")
    print square2

    # best way to operate on all elements because it's the clearest.
    square3 = [num*num for num in orig]
    print("Squares3: ")
    print square3
    printSeparator()
        
def conditionalOperatorsOnLists():
    
    numbers = [0,1,2,3,4,5]
    numsBelow4 = []
    
    # Basic way to do it
    for num in numbers:
        if num < 4:
            numsBelow4.append(num)
            
    
    # Can also use filter, which works like map like in listOfSquares
    # filter just accepts a conditional statement instead
    numsBelow4_v2 = filter(lambda x:x < 4,numbers)
    
    # How to use loops inside an array structure. Apparently this is clearest.
    numsBelow4_v3 = [num for num in numbers if num < 4 ]
    print "Find all numbers less than 4"
    print numsBelow4_v3
    
    printSeparator()

def whyMapAndFilterAreNotUseful():
    
    # This combines using map and filter. Find all squares that are under 20
    numbers = [0,1,2,3,4,5]
    
    print "Find all squares less than 20"
     
    # Starting to get longer and longer horizontally       
    squaresBelow20 = filter(lambda x:x<20, map(lambda y:y*y,numbers))
    print squaresBelow20
    
    # The best way to do it. Much more readable than map and filter.
    squaresBelow20_v2 = [num*num for num in numbers if num*num < 20]
    print squaresBelow20_v2
    
    # Disadvantages of doing it the "cleaner" way: The entire array needs to be stored in memory at once!
    # This is called "List Comprehensions" though.
    
    # The other way to do it is by "Generator Expressions" which basically means putting parenthesis 
    # Instead of square brackets. But this way, it only pulls one value at a time instead of
    # storing the entire array.
    squaresBelow20_v3 = (num*num for num in numbers if num*num < 20)
    
    #Note you can't just "print" generator expressions
    print "Can't print generator expressions: "
    print squaresBelow20_v3
    
    print "Need to use a loop to figure out what the values are..?"
    for sq in squaresBelow20_v3:
        print sq
    
    print "However, once you print the generator expression, it's GONE! You can't print it again!"
    for sq in squaresBelow20_v3:
        print sq        
        
    # Not sure what the tut was getting at, but if you're calling a function with only a generator expression
    # you only need one set of parenthesis, ie: some_function(item for item in list)
    
    # Syntax definition
    # List comprehension has syntax: [element for variable(s) in list if condition] <- square brackets
    # Generator expression has syntax: (element for variable(s) in list if condition) <- parenthesis
    
    printSeparator()
    
    
def usingNestedForStatements():
    
    print "Using original loops"
    for x in xrange(4):
        for y in xrange(4):
            if x < y:
                print (x,y,x*y)
                
                
    # Matlab equivalent:
    # for x = 0:3
    # for y = 0:3
    # if x < y
    # disp([x y x*y])
    # end; end; end
    
    print "Using nested for loop"
    print [(x,y,x*y) for x in xrange(4) for y in xrange(4) if x < y]
    # You could technically put in as many "for"s as you want.
    
    printSeparator()
    
    
def iteratingOverAList():   
    
    alph = ['a','b','c','d','e']
    
    print "Really cool - enumerating over a list returns a PAIR - both the index and the value"
    for index,string in enumerate(alph):
        print index,string,
    
    printSeparator()
    
def checkingForOneOrAllConditionalMatches():
    
    numbers = [1,2,3,4,5,6,7,8]
    print numbers
    if [num for num in numbers if num < 6]:
        print "There is a num in numbers that is less than six."
        
    if [num for num in numbers if num > 10]:
        print "There's a number greater than 10"
    else:
        print "No number greater than 10"
        
    # Find at least one match
    if any(num < 5 for num in numbers):
        print "Array contains value less than 5"
        
    # Check for ALL matches
    if all(num < 10 for num in numbers):
        print "All values in array are less than 10"
        
def setIsUniqueInMatlab():
    
    numbers = [1,1,1,2,3,4,5,5]
    print len(numbers) == len(set(numbers))
    print set(numbers) # Not yet an array/list
    print list(set(numbers)) # Need to explicitly turn back into a list.

def printSeparator():
    print 
    print '%%%%%%%%%%%%%%%%%%%%%%'
    print 

def main():
    listOfSquares()
    conditionalOperatorsOnLists()
    whyMapAndFilterAreNotUseful()    
    usingNestedForStatements()
    
    iteratingOverAList()
    checkingForOneOrAllConditionalMatches()
    setIsUniqueInMatlab()

	
if __name__ == "__main__":
    print __name__
    main()