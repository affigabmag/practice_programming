// Exercise 5: Array Methods

// Task 1: Create an array called colors with: "red", "green", "blue"
// Add "yellow" to the end using push()
// Print the array
// TODO: Write your code here
let colors=["red", "green", "blue"]
colors.push("yellow")
console.log(colors)


// Task 2: Remove the last element from the colors array using pop()
// Print the array
// TODO: Write your code here
let c=colors.pop()
console.log(colors,c)


// Task 3: Create an array called numbers with: 10, 20, 30, 40, 50
// Use indexOf() to find the position of 30
// Print the position
// TODO: Write your code here
let numbers=[10, 20, 30, 40, 50]
let p=numbers.indexOf(30)
console.log(p)


// Task 4: Create an array called animals with: "cat", "dog", "bird"
// Check if "dog" is in the array using includes()
// Print true or false
// TODO: Write your code here
let animals=["cat", "dog", "bird"]
console.log(animals.includes("dog"))

// Task 5: Create an array called nums with: 1, 2, 3, 4, 5
// Use forEach() to print each number multiplied by 2
// TODO: Write your code here
let nums=[ 1, 2, 3, 4, 5]
nums.forEach((num,index)=>{console.log(num*2)});

