'''
Albert is stranded on a frozen lake. He wants to know if he can make it back to shore. He is currently on a snowbank that gives him some traction,
but once he steps on the ice, he will slide in the same direction until he hits another snowbank.
There are also treacherous holes in the ice that he must avoid. As a cruel twist of fate, Albert's young pup, Kuna, is also stranded,
but on a different snowbank. Can Albert reach his pup AND make it to shore? Albert can only move horizontally and vertically.
He makes it to shore by leaving the lake grid Input Format side length the length of a side of the lake (it's a square)
lake grid a 2D matrix representing the lake 0 ice, 1 snowbank, -1 hole albert row row of Albert's snowbank albert column column of Albert's
snowbank kuna row row of Kuna's snowbank kuna column column of Kuna's snowbank Output Format integer True if he escapes with pup, False if he does not
'''

def findMin(array):
    ans = []
    localMin(array, 0, 0, len(array)-1, len(array), ans)
    return ans

def localMin(array, topLeftX, topLeftY, height, N, ans):
    if height<=1:
        testForLocalMinimum(array,topLeftX,topLeftY,N, ans);
        return;

    localMin(array,topLeftX,topLeftY,height/2,N, ans)
    localMin(array,topLeftX+(height/2)+1,topLeftY, height/2,N, ans)
    localMin(array,topLeftX, topLeftY +(height/2) + 1,height/2,N, ans)
    localMin(array,topLeftX+(height/2)+1,topLeftY +(height/2) + 1,height/2,N, ans)

def testForLocalMinimum(array, topLeftX, topLeftY, N, ans):
    isLocalMinimum(array,topLeftX,topLeftY,N, ans)
    isLocalMinimum(array,topLeftX+1,topLeftY,N, ans)
    isLocalMinimum(array,topLeftX,topLeftY+1,N, ans)
    isLocalMinimum(array,topLeftX+1,topLeftY+1,N, ans)

def isLocalMinimum(array, rowIndex, colIndex, N, ans):
    topRowIndex = rowIndex-1
    bottomRowIndex = rowIndex+1
    leftColIndex = colIndex-1
    rightColIndex = colIndex+1;
    foundLocalMinimum = True
    if -1 < topRowIndex and topRowIndex < N:
        if array[rowIndex][colIndex] >= array[topRowIndex][colIndex]:
            foundLocalMinimum = False

    if -1 < bottomRowIndex and bottomRowIndex < N:
        if array[rowIndex][colIndex] >= array[bottomRowIndex][colIndex]:
            foundLocalMinimum = False

    if -1 < leftColIndex and leftColIndex < N:
        if array[rowIndex][colIndex] >= array[rowIndex][leftColIndex]:
            foundLocalMinimum = False

    if -1 < rightColIndex and rightColIndex < N:
        if array[rowIndex][colIndex] >= array[rowIndex][rightColIndex]:
            foundLocalMinimum = False

    if foundLocalMinimum:
        ans.append(rowIndex)
        ans.append(colIndex)

arr = [[0,2,4,6], [3,5,2,7], [7,3,6,1], [5,1,3,8]]
print findMin(arr)

