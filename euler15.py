import time
 
def recPath(gridSize):
    """
    Recursive solution to grid problem. Input is a list of x,y moves remaining.
    """
    # base case, no moves left
    if gridSize == [0,0]: return 1
    # recursive calls
    paths = 0
    # move right when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1,gridSize[1]])

    # move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0],gridSize[1]-1])
 
    return paths

def main():
    gridSize = [0,3]
    result = recPath(gridSize)
    print result
    

	
if __name__ == "__main__":
    print __name__
    main()