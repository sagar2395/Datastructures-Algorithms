def longest_palindrome(str):
    res = ""
    resLength = 0
    
    for i in range(len(str)):
        l, r = i, i
        # Odd length
        while l >= 0 and r < len(str) and str[l] == str[r]:
            if(r - l + 1) > resLength:
                res = str[l:r+1]
                resLength = r - l + 1
            l -= 1
            r += 1
            
        # Even length
        l, r = i, i+1
        
        while l >= 0 and r <len(str) and str[l] == str[r]:
            if(r - l + 1) > resLength:
                res = str[l:r+1]
                resLength = r - l + 1
                
            l -= 1
            r += 1
            
    return res
            
str = "babad"
print(longest_palindrome(str))