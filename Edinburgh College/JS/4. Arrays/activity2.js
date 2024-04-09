// Sample test data
const sample_array = [20, 30, 25, 35, -16, 60, -100];
let add_data = 0;   // Initialise variable
// Sum data in array, looping each element
for (let i = 0; i < sample_array.length; i++) {
    add_data += sample_array[i];
}
let average = add_data / sample_array.length;
console.log(`Average value of the array elements is: ${average.toFixed(1)}.`);