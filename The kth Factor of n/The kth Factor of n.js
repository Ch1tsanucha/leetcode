/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthFactor = function(n, k) {

    let arr=[]
    
    for(let i = 1;i<n+1;i++){
      if(!(n%i)){
        arr.push(i)
      }
    }
    
    if(k>arr.length){
     return(-1)
    }
    else{
    return(arr[k-1])
    }
    
    
    };