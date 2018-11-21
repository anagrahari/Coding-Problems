'''
Given a matrix. Design an algorithm to find local minima. i.e. strictly smaller than all of its four neighbours
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

