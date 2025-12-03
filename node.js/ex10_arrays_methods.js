// Exercise 10: Array Methods

// Task 1: Use map() to double each number in an array
// Create an array: [1, 2, 3, 4, 5]
// Use map() to create a new array where each number is doubled
// Print the result
// TODO: Write your code here
let arr1=[1,2,3,4,5]
let arr2=[]
for (c=0;c<arr1.length;c++)
{
    arr2.push(arr1[c]*2);
    console.log(`arr1: ${arr1[c]} arr2: ${arr2[c]}`)
}

// Task 2: Use filter() to get only even numbers
// Create an array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// Use filter() to create a new array with only even numbers
// Print the result
// TODO: Write your code here
let arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let arreven=[]

function filter()
{
    for (c=0;c<arr.length;c++)
        {
            if (arr[c]%2==0) arreven.push(arr[c]);
        }
}

function print()
{
    console.log(arreven);
}

filter();
print();

//////////////////////////////////////////////////////
// method 2
//////////////////////////////////////////////////////
let arrt2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let arrevent2=arrt2.filter(num=> num % 2 ===0);
console.log(arrevent2);


// Task 3: Use reduce() to sum all numbers in an array
// Create an array: [1, 2, 3, 4, 5]
// Use reduce() to add all numbers together
// Print the result (should be 15)
// TODO: Write your code here
let arrt3=[1, 2, 3, 4, 5]
let sum=arrt3.reduce((acc,num)=>{
            return acc+num;
        },0);

console.log(sum);

// Task 4: Use find() to get the first number greater than 5
// Create an array: [2, 4, 6, 8, 10, 12]
// Use find() to get the first number greater than 5
// Print the result (should be 6)
// TODO: Write your code here
let arrt4=[2, 4, 6, 8, 10, 12]
let res=arrt4.find(num=> num>5)
console.log(res)

// Task 5: Use some() and every() methods
// Create an array: [2, 4, 6, 8, 10]
// Use some() to check if any number is greater than 7
// Use every() to check if all numbers are even
// Print both results
// TODO: Write your code here
let arrt5=[2, 4, 6, 8, 11]
let res1=arrt5.some(num=> num>7)
console.log(res1)
let res2=arrt5.every(num=>num % 2===0)
console.log(res2)
