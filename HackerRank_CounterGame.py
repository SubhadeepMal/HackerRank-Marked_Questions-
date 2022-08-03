import math
def counterGame(n):
    # Write your code here
    c=0
    l=["Louise","Richard"]
    while n!=1:
        m=n-2**(math.log(n)//math.log(2))
        if m!=0:
            n=m
        else:
            n=n/2
        if n!=1:
            c+=1
    return l[c%2]