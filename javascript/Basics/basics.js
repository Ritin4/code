/* 
Problem: Implement max(), min(), and sum() manually using raw
primitive loops; avoid all built-ins.
*/

//=============== Maximum ==============

function maximun(arr) {
    let max_ = -Infinity
    for (let i=0; i< arr.length; i++){
        if(arr[i] > max_){
            max_ = arr[i]
        }
    }
    return max_
}

console.log(maximun([1,2,3,4,5]))

//=============== Minimum ==============

function minimum(arr) {
    let min_ = Infinity
    for (let i=0; i< arr.length; i++){
        if(arr[i] < min_){
            min_ = arr[i]
        }
    }
    return min_
}

// console.log(minimum([1,2,3,4,5]))

//=============== Sum ==============

function Sumofnumbers(arr) {
    let sum_ = 0
    for (let i=0; i< arr.length; i++){
        sum_ = arr[i] + sum_
    }
    
    return sum_
}

console.log(Sumofnumbers([1,2,3,4,5,6,7,8,9,10]))