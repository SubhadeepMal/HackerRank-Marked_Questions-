#HackerRank: Number Arrangements
from itertools import permutations
def numberOfTimesOccured(A,B):
    k=[d for d in A]
    l=list(permutations(k))
    #print(l)
    q=[]
    for x in l:
        h=""
        for f in x:
            h+=f
        q.append(h)
    print("Permutation of arrangements: ",q)
    p=len(B)
    n=0
    print("Possible matches: ")
    for x in range(0, p-len(A)+1):
        j=""
        for y in range(len(A)):
            j+=B[x+y]
        #print(j)
        if j in q:
            n+=1
            print(j) 
    return n

A=input()
B=input()
print(numberOfTimesOccured(A,B))