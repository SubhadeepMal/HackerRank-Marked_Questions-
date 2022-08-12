def palindrome(s):
    if s[0:len(s)]==s[-1:-(len(s)+1):-1]:
        return -1
        #return 0
def palindromeIndex(s):
    if palindrome(s)==-1:
        return -1
    # print(list(s[1:len(s)-1]))
    for x in range(len(s)):
        l=list(s[1:len(s)-1])
        # print(l)
        l.pop(x)
        # print(l)
        if palindrome(l) ==-1:
            break
    return x        

i=input("Enter input: ")
print(palindromeIndex(i))