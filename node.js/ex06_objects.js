// Exercise 6: Objects

// Task 1: Create an object called person with properties: name, age, city
// Set values: "John", 25, "New York"
// Print the entire object
// TODO: Write your code here
let person ={
    name:"john",
    age: 25,
    city: "new york"
};
console.log(person);

// Task 2: Access the name property from the person object
// Print it using dot notation (person.name)
// TODO: Write your code here
console.log(person.name);


// Task 3: Access the age property from the person object
// Print it using bracket notation (person["age"])
// TODO: Write your code here
console.log(person["age"]);


// Task 4: Create an object called car with properties: brand, model, year
// Set values: "Toyota", "Camry", 2022
// Add a new property color with value "red"
// Print the entire object
// TODO: Write your code here
let car={
        brand: "toyata",
        model: "camry",
        year: 2022
};
car.color="red";
console.log(car)

// Task 5: Create an object called book with properties: title, author, pages
// Set values: "JavaScript Guide", "John Doe", 350
// Change the pages property to 400
// Print the object
// TODO: Write your code here
let book={
    title: "javascript guide",
    author: "john doe",
    pages: 350
};
book.pages=400
console.log(book)
