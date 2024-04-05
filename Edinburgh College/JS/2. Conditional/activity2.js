firstNumber = Number(prompt("First number: "))
secondNumber = Number(prompt("Second number: "))
thirdNumber = Number(prompt("Third number: "))

if (secondNumber > firstNumber) {
    if (thirdNumber > secondNumber) {
        console.log("Increasing order")
    } else {
        console.log("Neither increasing or decreasing order")
    }
} else if (secondNumber < firstNumber) {
    if (thirdNumber < secondNumber) {
        console.log("Decreasing order")
    } else {
        console.log("Neither increasing or decreasing order")
    }
}