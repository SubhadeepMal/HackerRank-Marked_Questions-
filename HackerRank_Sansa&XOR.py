
'''
# Brute Force solution: O(n^2)
def sansaXor(arr):
    l=list(arr)
    for x in range(len(arr)):
        a=arr[x]
        for y in range(x+1, len(arr)):
            a^=arr[y]
            l.append(a)
    s=l[0]
    for x in l[1:]:
        s=s^x
    return s
'''
# More Optimised solution: O(n)
def sansaXor(arr):
    s=0
    if len(arr)%2==0:
        return 0
    for x in range(0, len(arr),2):
        s^=arr[x]
    return s

t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = sansaXor(arr)
    print(result)

    # Write your code here
