import numpy as np
import scipy.spatial

def apprentice():
    
    print"\n Apprentice level exercises \n"
    
    # Make an array read-only
    Z = np.random.random((3,3))
    Z.flags.writeable  = False
    # Z[1][1] = 2 <- will fail, "assignment destination is read-only
    
    # Create a 10x2 x,y coordinate system and convert them into polar coordinates
    Z = np.random.random((10,2))
    X,Y = Z[:,0],Z[:,1]
    print "X,Y coordinates"
    print X,Y
    R = np.sqrt(X**2 + Y**2)
    T = np.arctan2(Y,X)
    print "R,theta coordinates"
    print R,T
    
    print "\n"
    # Create randomized vector, replace max value with 0
    # For it to work on a matrix, you need to turn the index into a subscript
    R = np.random.random(4)
    print R
    # Note that counting goes across rows, unlike MATLAB which goes down columns
    print R.argmax()
    R[R.argmax()] = 0
    print R
    
    # Using meshgrid
    print "\n Using meshgrid"
    # Kind of like maxing a structure
    # MATLAB Z.x = zeros(10,10); Z.y = zeros(10,10);
    # PYTHON Z['x'], Z['y'] are the fields that exist
    Z = np.zeros((4,4),[('x',float),('y',float)])
    sz = np.shape(Z['x'])
    Z['x'],Z['y'] = np.meshgrid(np.linspace(0,1,sz[0]),np.linspace(0,1,sz[1]))
    print Z['x'], "\n", Z['y']
    
    # Print max/min for all numpy scalar types
    print "\n int info, np.int8,int32,int64"
    for dtype in [np.int8,np.int32,np.int64]:
        print np.iinfo(dtype).min
        print np.iinfo(dtype).max
        
    print "float32,float64 info"
    for dtype in [np.float32, np.float64]:
        print np.finfo(dtype).min
        print np.finfo(dtype).max
        print np.finfo(dtype).eps        
  
    # Create a structured array representing a position (x,y) and a color (r,g,b)
    # Seriously, watch out for commas at the end of these freakign structures
    Z = np.zeros(10,[('position', [('x',float, 1),
                                  ('y',float, 1)]),
                     ('color',      [('r',float, 1),
                                    ('g',float, 1),
                                    ('b', float, 1)])])
                              
    # How to access different parts of the array.
    Z['color']['r'][3] = 2
    Z['position']['y'][0] = 15
    print "\n",Z
    
    # Get the distance between points
    Z = np.random.random((10,2))
    X,Y = np.atleast_2d(Z[:,0]), np.atleast_2d(Z[:,1])
    # ARRAY.T = transverse (ARRAY' in MATLAB)
    # Subtracting a row with a column gives you a matrix of all the combinations
    
    
    # Printing an array more prettily
    np.set_printoptions(precision = 3)
    print "\n Subtracting a row vector with a column vector gives all possible combos"
    print X - X.T
    print "\n This is the distance matrix"
    print np.sqrt((X-X.T)**2 + (Y-Y.T)**2)
    
    # Using scipy will make this faster. Note that you actually have to import scipy.spatial
    print "\n This is the distance matrix x2"    
    print scipy.spatial.distance.cdist(Z,Z)
    
    # Find the nearest value from a given value in an array
    Z = np.random.uniform(0,1,(5,5))
    val2match = 0.5
    print "\n Random vector. Find nearest val to 0.5 \n",Z
    # Note that argmin() gives a pure index, counted by rows, not by columns
    print Z.flat[abs(Z - val2match).argmin()]
    
def novice():
    
    print"\n Novice level exercises \n"
    
    Z = np.zeros((8,8),dtype = int)
    # Fill 8x8 matrix with checkerboard pattern
    # Keep in mind that 1 = the SECOND row!
    Z[1::2,::2] = 1                     # Z(2:2:end,1:3:end) = 1
    Z[::2,1::2] = 2
    print "Z[1::2,::2] = 1;Z[::2,1::2] = 2]"
    print Z 
    print "\n\n"
    
    # Create 10x10 matrix with random, find min/max
    R = np.random.random((10,10))
    Rmin,Rmax = R.min(), R.max()
    
    # Normalize the matrix
    R = (R-Rmin)/(Rmax-Rmin)
    
    # Use "tile" to create checkerboard
    print np.tile( np.array([[1,0],[0,1]]), (4,4) )         #repmat([1 0; 0 1],[4 4])
    
    # Real matrix product
    np.dot(np.ones((5,3)),np.ones((3,2)))                       #ones(5,3) * ones(3,2)
    
    # Create a 5x5 matrix from values ranging from 0-4
    Z = np.zeros((5,5))
    Z += np.arange(5)
    
    print "\n"
    print "Z = np.zeros((5,5)); Z += np.arange(5)"
    print Z
    
    # Create a vector, size 10, ranging 0:1, both values excluded
    # [1:-1] excludes the 0th index and the end-1th index
    V = np.linspace(0,1,12,endpoint = True)[1:-1]               # a = linspace(0,1,12); a(2:end-1)
    print "\n"
    print V
    
    # Sorting 
    R = np.random.random((3,3))
    print "\n"
    print R
    print "np.sort(R,axis=None)"
    print np.sort(R,axis=None)
    print "np.sort(R,axis=1)"    
    print np.sort(R,axis = 1)
  
    # Are matrices equal?
    # randint: Random integer between 0 <= x < 3; (5,5) sized matrix
    A = np.random.randint(0,3,(5,5))
    print A
    B1 = np.random.randint(0,2,3)
    B2 = np.random.randint(0,2,3)
    print "B1,B2"
    print B1,B2
    print "Are B1, and B2 the same?"
    print np.allclose(B1,B2)        
    
    
    

def basics():
    
    print"\n Basic level exercises"    
    
    # Indexing for matrices starts at zero
    Z = np.zeros((2,3,4))                         # zeros(3,4)
    # Indexing individual variables (assuming i,j,k) goes in (k,i,j)
    Z[1,2,1] = 3                                # Z(4,1,2) = 3
    
    print Z
    
    # It doesn't appear that numpy can do more than 3D matrices
    Z2 = np.zeros((3,2,4,5))                    # zeros(4,5,6); last dimension is concatenated
    
    R = np.arange(10,50)                        # R = 10:49
    
    # Reshape goes along rows instead of columns.
    R = np.arange(9).reshape(3,3)               # reshape(1:9,3,3)
    print "\n Reshaping along a row\n", R
    # np.dot is for matrix multiplication. Guess it's related to doing the dot product..?
    print np.dot(R,R)
    # * is standard vector multiplication
    print R*R
    
    #array([[0, 1, 2],
    #   [3, 4, 5],
    #   [6, 7, 8]])
    
    # When using np.nonzero, nz comes out as a list NOT a matrix!
    R = np.array([3,8,0,5,0])
    nz = np.nonzero(R)                # find(mat ~= 0)
    print "\n When using np.nonzero, nz comes out a little weirder",nz
    print nz[0][1]
    print R[nz]
    
    nz += np.ones((1,len(nz)))
    print nz
    
    
    
def matrixLogistics():
    
    R = np.random.random((5,5))
    
    print "\n Get a random matrix...: \n"
    print R                          # Random matrix
    # Note that to actually access it, you need to use R.flat(R.argmin())
    # Or, you could just use R.min()
    print "\n Find the index of the global min"
    print R.argmin(), R.min()
    print "\n Find the min along the columns"
    print R.argmin(axis=0)
    print "\n Find the min along the rows"
    print R.argmin(axis=1)
    #print "\n concatenate along columns"
    #print np.hstack([R,R])
    #print "\n concatenate along rows"
    #print np.vstack([R,R])
    #print "\n concatenate along desired dimension, but a little weird"
    #print np.dstack([R,R])
    
    # Probably a better way to concatenate? More like images. This is mostly because when you have
    # a 3D array, it corresponds to the first axis now...kind of weird.
    #R2 = np.zeros((2,5,5))
    #R2[0,:,:] = R
    #print R2
    
    print "\n Print second col"    
    print R[:,1]
    print "\n Print last row"              # print A[-1,:] = print last row   
    print R[-1,:]
    
    # Iterating over matrices
    # Default is to iterate over the first index
    #for row in R:
    #    print "Iterating goes over rows: ", row
        
    # Note that flat is not a function call, similar to T for transverse
    #for element in R.flat:
    # print element
    
    # Get all rows with the second index < 0.5
    print "\n Get all rows where first column index is less than 0.5: \n"
    # It looks like conditional indexing works pretty similarly to MATLAB which is good.
    print R[R[:,0] < 0.5,:]
        
                        

def printSeparator():
    
    print "\n %%%%%%%%%%%%%%%%%%%%% \n %%%%%%%%%%%%%%%%%%%%% \n"
    

def main():
    basics()
    printSeparator()
    matrixLogistics()
    #printSeparator()
    #novice()
    #printSeparator()
    #apprentice()
    


if __name__ == "__main__":
    main()