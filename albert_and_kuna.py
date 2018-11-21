'''
Albert is stranded on a frozen lake. He wants to know if he can make it back to shore. He is currently on a snowbank that gives him some traction,
but once he steps on the ice, he will slide in the same direction until he hits another snowbank.
There are also treacherous holes in the ice that he must avoid. As a cruel twist of fate, Albert's young pup, Kuna, is also stranded,
but on a different snowbank. Can Albert reach his pup AND make it to shore? Albert can only move horizontally and vertically.
He makes it to shore by leaving the lake grid Input Format side length the length of a side of the lake (it's a square)
lake grid a 2D matrix representing the lake 0 ice, 1 snowbank, -1 hole albert row row of Albert's snowbank albert column column of Albert's
snowbank kuna row row of Kuna's snowbank kuna column column of Kuna's snowbank Output Format integer True if he escapes with pup, False if he does not
'''


def findPath(array, aX, aY, dX, dY):
    return findAll(array, aX, aY, dX, dY)

def findAll(array, aX, aY, dX, dY):
    return findLeft(array, aX, aY-1, dX, dY) or findRight(array, aX, aY+1, dX, dY) or findBottom(array, aX+1, aY, dX, dY) or findTop(array, aX-1, aY, dX, dY)

def findLeft(array, x,y,dX, dY):
 #   print 'Left', dX,dY,x,y
    if y < 0:
        return False
    if array[x][y] ==2:
        return False
    if x== dX and y==dY:
        return True
    if array[x][y] == 1:
        return findAll(array,x,y,dX,dY)
    if array[x][y] == -1:
        return False
    if array[x][y] == 0:
        array[x][y] = 2
        return findLeft(array, x, y-1, dX,dY)

def findRight(array, x, y,dX,dY):
  #  print 'right', dX,dY,x,y
    if y >= len(array[0]):
        return False
    if array[x][y] ==2:
        return False
    if x== dX and y==dY:
        return True
    if array[x][y] == 1:
        return findAll(array,x,y,dX,dY)
    if array[x][y] == -1:
        return False
    if array[x][y] == 0:
        array[x][y] = 2
        return findRight(array, x, y+1,dX,dY)

def findBottom(array, x, y,dX,dY):
 #   print 'bottom', dX,dY,x,y
    if x >= len(array):
        return False
    if array[x][y] ==2:
        return False
    if x== dX and y==dY:
        return True
    if array[x][y] == 1:
        return findAll(array,x,y,dX,dY)
    if array[x][y] == -1:
        return False
    if array[x][y] == 0:
        array[x][y] = 2
        return findBottom(array, x+1, y,dX,dY)

def findTop(array,x, y,dX,dY):
   # print 'top', dX,dY,x,y
    if x < 0:
        return False
    if array[x][y] ==2:
        return False
    if x== dX and y==dY:
        return True
    if array[x][y] == 1:
        return findAll(array,x,y,dX,dY)
    if array[x][y] == -1:
        return False
    if array[x][y] == 0:
        array[x][y] = 2
        return findTop(array, x-1, y,dX,dY)


a = [[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,0,1,-1,0,-1,0],[-1,0,0,0,0,0,0],[0,0,1,0,0,1,0],[-1,0,-1,0,-1,0,0],[0,0,0,0,0,0,0]]
print findPath(a,4,2,4,6)

