/* function sayHello() {
  console.log("Hello world");
}

function greet(name = "you") {
  console.log(`Hello ${name}`);  // Remember to use `` to use in-line variable in string
}

function add(x, y) {
  console.log(x + y);
  return x + y;
}

function changeNumber(number) {
  number = 456;
  console.log(`number is ${number}`);
}

sayHello();
greet("Gary");
let sum = add(3, 4);
console.log(sum)
greet();
changeNumber(234);
*/

// let myArray = [7, "hello", "world", 12, true, 100, "yay"];
// myArray.push("howdy")
// console.log(myArray);

// console.log(myArray.indexOf("yay"));
// console.log(myArray.indexOf(200));  // returns -1 if not in array

// let array1 = ["hello", "world"];
// let array2 = ["we", "love", "JS"];

// let array3 = array1.concat(array2);

// console.log(array3);

let groceries = [
  {name: "bread", price: 0.85},
  {name: "milk", price: 1.09},
  {name: "eggs", price: 1.10},
  {name: "juice", price: 3.20},
  {name: "pasta", price: 1.75},
  {name: "lemon", price: 0.30}
]

// let cheapGroceries = groceries.filter((item) => {
//   return item.price <= 1;
// });

// console.log(cheapGroceries);

// // return the names
// let itemNames = groceries.map((item) => {
//   return item.name;
// });

// console.log(itemNames);

// print each item in separate lines
// groceries.forEach((item) => {
//   console.log(item.name);
// });

// let sum = 0;

// for (let i = 0; i < 10; i++) {
//   sum = sum + i;
// }
// console.log("Sum = " + sum);

// for (let i = 0; i < groceries.length; i++) {
//   console.log(groceries[i].name)
// }

// for (let item of groceries) {
//   console.log(item.name)
// }
