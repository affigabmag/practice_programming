// Exercise 7: Functions

// Task 1: Create a function called greet that takes a name parameter
// The function should print "Hello, [name]!"
// Call the function with "Alice"
// TODO: Write your code here
function greet(name)
{
    console.log(`Hello, ${name}!`);
}
greet("alice");

// Task 2: Create a function called add that takes two parameters (a, b)
// The function should return the sum of a and b
// Call the function with 5 and 10, print the result
// TODO: Write your code here
function add(a,b)
{
    return a+b;
}
console.log(add(5,10))

// Task 3: Create a function called multiply that takes two parameters (x, y)
// The function should return the product of x and y
// Call the function with 4 and 7, print the result
// TODO: Write your code here
function multiply(x,y)
{
    return x*y
}
console.log(multiply(4,7))


// Task 4: Create a function called getLength that takes a string parameter
// The function should return the length of the string
// Call the function with "JavaScript", print the result
// TODO: Write your code here
function getLength(str)
{
    return str.length;
}
console.log(getLength("gabriel"))


// Task 5: Create a function called isEven that takes a number parameter
// The function should return true if the number is even, false if odd
// Call the function with 10 and 7, print both results
// TODO: Write your code here
function isEven(num)
{
    if (num % 2 === 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

console.log(isEven(7))
console.log(isEven(10))

