const convertBtn = document.getElementById("convert-btn");
const number = document.getElementById("number");
const output = document.getElementById("output");

const checkUserInput = () => {
    const inputNumber = parseInt(number.value);
    // 4.When you click on the #convert-btn element without entering a value into the #number element, the #output element should contain the text Please enter a valid number
    if (!number || isNaN(inputNumber)) {
        invalid();
        output.textContent = "Please enter a valid number";
        return;
    } else if (inputNumber < 1) {
        // 5.When the #number element contains the number -1 and the #convert-btn element is clicked, the #output element should contain the text Please enter a number greater than or equal to 1
        invalid();
        output.textContent = "Please enter a number greater than or equal to 1";
        return;
    } else if (inputNumber > 3999) {
        // 6.When the #number element contains the number 4000 or greater and the #convert-btn element is clicked, the #output element should contain the text Please enter a number less than or equal to 3999
        invalid();
        output.textContent = "Please enter a number less than or equal to 3999";
        return;
    } else {
        romanNumeral(inputNumber);
    }
};

const romanNumeral = (number) => {
    if (output.classList.toggle("hidden")) {
        output.classList.toggle("hidden");
    }
    output.style.backgroundColor = "var(--grey)";
    output.style.color = "var(--white)";
    output.style.borderColor = "var(--white)";
    let result = "";
    for (let i = number; i > 0; i--) {
        result += "I";
        if (result.match(/(?<![V])IIII/g)) {
            result = result.slice(0, -3) + "V";
        } else if (result.match(/IVI/g)) {
            result = result.slice(0, -3) + "V";
        } else if (result.match(/VIIII/g)) {
            result = result.slice(0, -5) + "IX";
        } else if (result.match(/IXI/g)) {
            result = result.slice(0, -3) + "X";
            if (result.match(/XXXX/g)) {
                result = result.slice(0, -3) + "L";
            } else if (result.match(/XLX/g)) {
                result = result.slice(0, -3) + "L";
            }
        }
        if (result.match(/LXL/g)) {
            result = result.slice(0, -3) + "XC";
        } else if (result.match(/XCX/g)) {
            result = result.slice(0, -3) + "C";
        }
        if (result.match(/CCCC/g)) {
            result = result.slice(0, -3) + "D";
        } else if (result.match(/CDC/g)) {
            result = result.slice(0, -3) + "D";
        }
        if (result.match(/DCD/g)) {
            result = result.slice(0, -3) + "CM";
        } else if (result.match(/CMC/g)) {
            result = result.slice(0, -3) + "M";
        }
    }
    output.textContent = result;
};

const invalid = () => {
    if (output.classList.toggle("hidden")) {
        output.classList.toggle("hidden");
    }
    output.style.backgroundColor = "#ffaaaa";
    output.style.color = "#990000";
    output.style.borderColor = "990000";
};

convertBtn.addEventListener("click", checkUserInput);

number.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        checkUserInput();
    }
});

/* 
7.When the #number element contains the number 9 and the #convert-btn element is clicked, the #output element should contain the text IX ✓
8.When the #number element contains the number 16 and the #convert-btn element is clicked, the #output element should contain the text XVI ✓
9.When the #number element contains the number 649 and the #convert-btn element is clicked, the #output element should contain the text DCXLIX ✓
10.When the #number element contains the number 1023 and the #convert-btn element is clicked, the #output element should contain the text MXXIII ✓
11.When the #number element contains the number 3999 and the #convert-btn element is clicked, the #output element should contain the text MMMCMXCIX ✓
*/
