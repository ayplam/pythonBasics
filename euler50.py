import numpy as np
import time

def getAllPrimes(num):

    arr = [];
    
    nums2check = range(3,num,2)
    
    for num in nums2check:
        if isprime(num):
            arr.append(num) 
 
        
    arr.append(2)       
    return arr     
        
    
def isprime(num):
    
    chk = np.mod(num,range(2,num,1))
        
    return not any(div==0 for div in chk)
    
def main():
    
    t = time.time()
    
    val = 20
    tot = 0
    prim = 0
    
    while tot < 10000:
        arr = getAllPrimes(val)
        tot = np.sum(arr)
        
        if isprime(tot) and tot < 10000:
            prim = tot
            print prim
            print arr
            
        val += 2
    
    print prim    
    
    print time.time() - t    
	
if __name__ == "__main__":
    print __name__
    main()