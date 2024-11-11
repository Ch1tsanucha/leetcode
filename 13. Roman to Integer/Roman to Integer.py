class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        last = 0
        current = 0
        dic ={
            I:1,V:5,X:10,L:50,C:100,D:500,M:1000
        }
        for i in s:
            last = current
            output = output+ dic[i]
            current = dic[i]
            if(current > last):
                output = (output - (current+last)) + (current - last)
        return output
                
        
