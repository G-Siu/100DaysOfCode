let firstNumber = Number(prompt("First number: "))
let secondNumber = Number(prompt("Second number: "))
let thirdNumber = Number(prompt("Third number: "))

if (firstNumber == secondNumber && firstNumber == thirdNumber) {
    console.log("All numbers are equal")
} else if ((firstNumber == secondNumber && firstNumber != thirdNumber) || (firstNumber != secondNumber && firstNumber == thirdNumber)) {
    console.log("Neither all are equal or different")
} else {
    console.log("All numbers are different")
}
