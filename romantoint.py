#Taking strings that represent integers, transform them and return ints
#Negative numbers?
#All the strings will be only roman numerals
#A good idea would be to create a dictionary of the values and use a loop to check if the prior value is lower than the next.

class Solution:
    def romanToInt(self, s: str) -> int: 
        #Dictionary to map the values       
        mydict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }            
        val = 0              
        for i in range(len(s)):
            current = mydict[s[i]]
            if i<len(s)-1 and current<mydict[s[i+1]]:
                val-=current
            else:
                val+=current
        return val
