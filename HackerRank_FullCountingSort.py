# HackerRank Full CountSort:

def countSort(arr):
    s=[[] for i in range(100)]
    n=len(arr)
    for x in range(n//2):
        s[int(arr[x][0])].append('-')
    for y in range(n//2,n):
        s[int(arr[y][0])].append(arr[y][1])
    for string in s:
        if string:
            print(*string, end=' ')
        # The star(*) operator unpacks the sequence/collection into -
        # positional arguments. So if you have a list and want to pass the -
        # items of that list as arguments for each position as -
        # they are there in the list, instead of indexing each -
        # element individually, you could just use the * operator.

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(input().rstrip().split())

countSort(arr)
