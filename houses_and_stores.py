'''You are given two arrays representing integer locations of stores and houses (each location in this problem is one-dimensional).
For each house, find the store closest to it. Write a function: vector〈int> &houses) s olution (vectorínt> &stores, vector住nt> that,
given two arrays: stores of length M representing integer locations of the stores houses of length N representing integer locations of
the houses returns an integer array of size N. The i-th element of the returned array should denote the location of the store closest to the i-th house.
If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores
and houses at the same location. Assume that: . M and N are integers within the range [1..1,000]; . each element of arrays stores, houses is an integer
within the range [0.1,000,000]
'''

def house_store(house, st):
    store = list(st)
    store.sort()
    ans = []
    for index, val in enumerate(house):
        ans.appned(binary_search(store,val))
    return ans

def binary_search(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        if sequence[mid] < value:
            if mid +1 >= len(sequence): return sequence[mid]
            if abs(sequence[mid]-value) <= abs(sequence[mid+1]-value):
                return sequence[mid]
            lo = mid + 1
        elif value < sequence[mid]:
            if mid-1 < 0: return sequence[mid]
            if abs(sequence[mid]-value) < abs(sequence[mid-1]-value):
                return sequence[mid]
            if abs(sequence[mid]-value) == abs(sequence[mid-1]-value):
                return sequence[mid-1]
            hi = mid - 1
        else:
            return sequence[mid]


house=  [1,2,3,4,7,9,12,15,13,14,6,4,2,4,88,45,23]
store = [3,2,4,5,8,11,17,10,15,16,13,3,56,9,12,4,33]
house_store(house,store)
