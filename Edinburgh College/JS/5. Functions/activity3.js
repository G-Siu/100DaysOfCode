function primeNumber() {
    if (userNumber < 2) {
        console.log("Cannot be less than 2");
    } else {
        for (i = 2; i < userNumber; i++) {
            // If no remainder after division, number is not prime number
            if (userNumber % i == 0) {
                console.log(`${userNumber} is not a prime number`);
                return;
            } else {
                // Number is a prime number
                console.log(`${userNumber} is a prime number`);
                return;
            }
        }
        console.log(`${userNumber} is a prime number`);
    } 
}

// Get user number
const userNumber = Number(prompt("Enter a number: "));

// Run function with user input as parameter
primeNumber(userNumber)
