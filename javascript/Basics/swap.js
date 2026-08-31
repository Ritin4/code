/*
Problem:  Reverse array in-place
Input: array of elements
Output: array with reversed elements
*/

function reverseArr(arr){
    console.log("Started")
    for (let i=0, j=arr.length-1; i<arr.length - 1 && j>=0; i++,j--){
        console.log("Before arr[i]: ", arr[i])
        console.log("Before arr[j]: ", arr[j])

        arr[i] = arr[j]
        arr[j] = arr[i]

        console.log("After arr[i]: ", arr[i])
        console.log("After arr[j]: ", arr[j])

    }
    return arr
}

console.log(reverseArr([1,2,3,4,5]))