/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let low = 0;
let high = nums.length-1;
let middle = 0;

while(low <= high){
  middle = Math.floor((low + high) / 2);
    if(nums[middle] > target){
        high = middle-1
    }
    else if(nums[middle] < target){
        low = middle + 1
    }
    else{
   return middle;
    }
}
 return -1;
    
    
}