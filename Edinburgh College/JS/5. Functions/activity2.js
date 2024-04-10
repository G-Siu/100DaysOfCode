// Function to calculate factorial
function factorial(number) {
    let totalFactorial = 0;
    // Loop and add from 1 until the user input number
    for (let i = 1; i <= number; i++) {
        totalFactorial += i;
    }
    return totalFactorial;  // Return factorial for print
}

// Get input number
while (true) {
    const userNumber = Number(prompt("Enter a number: "));
    let toFactor = 0;
    if (userNumber < 0) {
        console.log("Cannot be a negative number.") // Loop again
    } else if (userNumber == 0) {
        toFactor = 1;
        console.log(factorial(toFactor));   // Print factorial of 1
        break;
    } else {
        toFactor = userNumber;
        console.log(factorial(toFactor));   // Calculate and print factorial
        break;
    }
}
