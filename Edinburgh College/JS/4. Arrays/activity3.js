// Sample data
const sample_array = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49];

// Sort sample array in descending order
let sorted_array = sample_array.sort().reverse();   
let maximum = sorted_array[0]; // Get maximum in array
let minimum = sorted_array[sample_array.length - 1]; // Get minimum in array
console.log(`Original Array: ${sample_array}`);
console.log(`Maximum value for the above array = ${maximum}`);
console.log(`Minimum value for the above array = ${minimum}`);
