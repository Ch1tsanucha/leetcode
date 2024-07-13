function isPalindrome(x: number): boolean {
    let loop : number = 0;
    for(loop=0;loop<x.toString().length-1;loop++){
        if(x.toString()[loop] != x.toString()[x.toString().length-1-loop]){
            return false
        }
    }
    return true
};