let land = ["Norge","Sverige","Danmark"];

let landFilter = land.filter(function(land){ 
    return land.startsWith("N") //if whats in the return thingy is true it will be added to the new array
})

console.log(landFilter)

let landMap = land.map(function(land){
    return land.toUpperCase() //goes through all the items and applies whatever says in the function to it and appends it to the new function
})

console.log(landMap)

let numbers = [1,2,3,4,5,6,7,8,9,10]

let numbersEven = numbers.some(function(numbers){
    return numbers%2 === 0 //will check if this can apply to any of the elements in the array, it returns True if atleast one of them are True
})

console.log(numbersEven)

//Can use .every the same way as .some, but then it will check if all the numbers can be applied to the statement 

land.forEach(function(land){
    console.log("Land:"+land) //same use as in C# 
})

