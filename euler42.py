import string
import os, glob


def getAlphDict():
    l1 = string.ascii_uppercase
    l2 = range(1,27)
    return dict(zip(l1,l2))
    
def getStringValue(string,alphabetDict):
    
    val = 0;
    for index,char in enumerate(string):
        val+=alphabetDict.get(char)
        
    return val
    
def getTriArray(val):
    
    arr = []
    val = 0
    n = 0;
    while val < 500:
        arr.append(0.5 * n * (n+1))
        n += 1
        val = arr[len(arr)-1]
    
    return arr
        
    
def isTriangularNumber(arr,val):
    
    return any(num == val for num in arr)       
    
def parseStrings(strings):
    
    tmp = strings.replace('"','')
    return tmp.split(',')


def main():

    alphabetDict = getAlphDict()
    triangularArr = getTriArray(500)
    
    os.chdir("C:\Users\Adrian Lam\Dropbox\DataIncubator\Python\Tutorials")
    f = open('p042_words (1).txt','r')
    
    allWords = parseStrings(f.readline())
    # print allWords
    
    numTriWords = 0
    
    for word in allWords:
        
        strVal = getStringValue(word,alphabetDict)
        
        if isTriangularNumber(triangularArr,strVal):
            numTriWords+=1
        
    
    
    f.close()
    
    print numTriWords




if __name__ == "__main__":
    print __name__
    main()