def ispalindrome(s,k):
    char_array = list(s)
    def ispalindrome_help(arr,swaps):
        if len(arr)<=1:
            return True
        elif len(arr)<=swaps:
            return True
        elif arr[0]==arr[len(arr)-1]:
            return ispalindrome_help(arr[1:len(arr)-1],swaps)
        else:
            found=False
            for i in range(swaps+1):
                if arr[i]==arr[len(arr)-1]:
                    found=True
                    swaps=swaps-i
                    arr=arr[i:]
                    break
            for i in range(swaps+1):
                if arr[0]==arr[len(arr)-(1+i)]:
                    found=True
                    swaps=swaps-i
                    arr=arr[0:len(arr)-i]
                    break
            if found == True:
                return ispalindrome_help(arr,swaps)        
            return False
    return ispalindrome_help(char_array,k)

def palin(s,k):
    i=0
    j=len(s)-1
    while i<j:
        if s[i] != s[j]:
            i+=1
            k-=1
        else:
            i+=1
            j-=1

    print(k)
    if k<0:
        return False
    else:
        return True
