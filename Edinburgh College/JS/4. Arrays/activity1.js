// Test data
const sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let add_data = 0;   // Initialise variable
// Sum data in array, looping each element
for (let i = 0; i < sample_array.length; i++) {
    add_data += sample_array[i];
}

console.log(`The sum is ${add_data}.`);   // Display sum