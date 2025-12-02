// Exercise 8: Loops

// Task 1: Create a for loop that prints numbers from 1 to 5
// TODO: Write your code here
for (let c=1;c<=5;c++)
{
    console.log(c);
}

// Task 2: Create a for loop that prints numbers from 10 down to 1
// TODO: Write your code here
for (let c=10;c>0;c--)
{
    console.log(c);
}


// Task 3: Create a while loop that prints numbers from 1 to 3
// TODO: Write your code here
let c=1
while (c<=3)
{
    console.log(c++);
}

// Task 4: Create a for loop that prints the characters of the string "Hello"
// Hint: Use string.length and string[index]
// TODO: Write your code here
let str="Hello";
for (let c=0;c<str.length;c++)
{
    console.log( str[c])
}


// Task 5: Create a for loop that adds up numbers in an array and prints the total
// Array: [1, 2, 3, 4, 5]
// Hint: Use array.length and array[index]
// TODO: Write your code here
let arr=[13,34245,453,74,885];
let t=0;
for (let c=0;c<arr.length;c++)
{
    t+=arr[c];
    console.log(`Current index ${c+1} Current arr compoment ${arr[c]} current summary ${t}`);
}