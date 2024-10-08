def longest_palindrome(s):
    res = ""
    resLength = 0
    
    for i in range(len(s)):
        l, r = i, i
        # Odd length
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if(r - l + 1) > resLength:
                res = s[l:r+1]
                resLength = r - l + 1
            l -= 1
            r += 1
            
        # Even length
        l, r = i, i+1
        
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if(r - l + 1) > resLength:
                res = s[l:r+1]
                resLength = r - l + 1
                
            l -= 1
            r += 1
            
    return res
            
s = "babad"
print(longest_palindrome(s))