// Exercise 9: Conditionals (if/else if/else)

// Task 1: Create a function that checks if a number is positive, negative, or zero
// Function name: checkNumber
// Parameter: num (a number)
// Return: "positive" if num > 0, "negative" if num < 0, "zero" if num === 0
// TODO: Write your code here
function checkNumber(num)
{
    if (num>0) return "Positive"
    if (num<0) return "Negative"
    if (num==0)  return "Zero" 
}

console.log(checkNumber(5))
console.log(checkNumber(-10))
console.log(checkNumber(0))

// Task 2: Create a function that grades a student based on their score
// Function name: gradeStudent
// Parameter: score (a number 0-100)
// Return: "A" if score >= 90, "B" if >= 80, "C" if >= 70, "D" if >= 60, "F" if < 60
// TODO: Write your code here
function gradeStudent(score)
{
    if (score>=90) return "A";
    if (score>=80) return "B";
    if (score>=70) return "C";
    if (score>=60) return "D";
    if (score<60) return "F";
}
console.log(gradeStudent(55))
console.log(gradeStudent(78))


// Task 3: Create a function that checks if a person can vote
// Function name: canVote
// Parameter: age (a number)
// Return: true if age >= 18, false otherwise
// TODO: Write your code here
function canVote(age)
{
    if (age>=18) return true 
    else return false;
}
console.log(canVote(15));
console.log(canVote(75));

// Task 4: Create a function that determines the day type
// Function name: dayType
// Parameter: day (a string like "Monday", "Saturday")
// Return: "Weekday" if Monday-Friday, "Weekend" if Saturday-Sunday
// Hint: Use day.toLowerCase() to handle any case
// TODO: Write your code here
function dayType(day)
{
    let d=day.toLowerCase();
    if (d=="monday" || d=="tuesday" || d=="wednesday" || d=="thursday" || d=="friday") return "Weekday";
    if (d=="saturday" || d=="sunday") return "Weekend";
}
console.log(dayType("sunday"));
console.log(dayType("monday"));


// Task 5: Create a function that checks the largest of three numbers
// Function name: findMax
// Parameters: a, b, c (three numbers)
// Return: the largest number
// TODO: Write your code here
function findMax(a,b,c)
{
    if (a>b && a>c) return a;
    if (b>a && b>c) return b;
    if (c>a && c>b) return c;
}
console.log(findMax(11,45,5))
console.log(findMax(11,5,1))
console.log(findMax(11,5,111))

