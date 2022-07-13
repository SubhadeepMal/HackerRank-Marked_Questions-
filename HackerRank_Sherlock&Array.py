

def balancedSums(arr):
    # Write your code here
    a=-1
    b=len(arr)
    s1=s2=0
    while (b-a) > 2:
        if s1<s2:
            a+=1
            s1+=arr[a]
        elif s2<s1:
            b-=1
            s2+=arr[b]
        else:
            if arr[a+1]<arr[b-1]:
                s1+=arr[a+1]
                a+=1
            elif arr[a+1]>arr[b-1]:
                s2+=arr[b-1]
                b-=1
            else:
                a+=1
                b-=1
                s1+=arr[a]
                s2+=arr[b]
    if s1==s2:
        return "YES"
    return "NO"
    

T = int(input().strip())

for T_itr in range(T):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = balancedSums(arr)
    print(result)
