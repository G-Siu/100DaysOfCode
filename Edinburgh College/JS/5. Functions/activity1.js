// Sample array
const sampleArray = [10, 2, 3, 4, 7];

// Function expression to display content in array
let arrayContent = function (array) {console.log(`The content of the array is: [${array}]`)};

// Max value function expression
let maxValue = function (array) {
    let sortedArray = sampleArray.sort((a,b)=>a-b).reverse(); // Sort by descending order
    console.log(`The max value in the array is: ${sortedArray[0]}`) // Display max value
};

arrayContent(sampleArray)
maxValue(sampleArray)


