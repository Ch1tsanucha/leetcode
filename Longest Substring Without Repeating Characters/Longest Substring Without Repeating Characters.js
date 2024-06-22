/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let arr=[]
    let max=0
    let r = 0
    let len = s.length
    
    while(r<len){
        if(arr.includes(s[r])){
            while(arr[0]!=s[r]){
                arr.shift();
            }
            if(arr[0]==s[r]){
                arr.shift();
            }
        }
        arr.push(s[r]);
        if(arr.length>max){
        max = arr.length
        }
        r++;
    
    }
    return max;
     
    };