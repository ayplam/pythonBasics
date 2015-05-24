import numpy as np

class Complex():
    def __init__(self,real,imag):
        self.r = real
        self.i = imag
        
    def mag(self):
         return np.sqrt(pow(self.r,2) + pow(self.i,2))
    

def printSeparator():
    print 
    print '%%%%%%%%%%%%%%%%%%%%%%'
    print 
          
def main():
    x = Complex(4,3)
    print [x.r,x.i]
    print x.mag()
    

	
if __name__ == "__main__":
    print __name__
    main()