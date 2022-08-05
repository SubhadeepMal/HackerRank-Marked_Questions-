## a+b=a^b

def sumXor(n):
    # Write your code here
    if n==0:
        return 1
    c=bin(n)[2:].count('0')
    return 2**c

n=int(input("Enter the number: "))
print(sumXor(n))