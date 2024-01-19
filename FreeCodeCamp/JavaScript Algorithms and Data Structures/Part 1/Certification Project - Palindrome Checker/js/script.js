function cleanInputString(str) {
    const regex = /[\W\s]/g;
    return str.replace(regex, "");
}

userInput = document.getElementById("text-input");
console.log(userInput);
// const inputResult = document.getElementByClassName('input-result');
// inputResult.innerText = `${}`
