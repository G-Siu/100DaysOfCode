function cleanInputString(str) {
    const regex = /[\W\s]/g;
    return str.replace(regex, "");
}

const checkBtn = document.getElementById("check-btn");

checkBtn.addEventListener("click", () => {
    const textInput = document.getElementById("text-input").value;
    const cleanInput = cleanInputString(textInput).toLowerCase();
    const reverseInput = cleanInput.split("").reverse().join("");
    const inputResult = document.getElementById("result");
    if (cleanInput === reverseInput) {
        inputResult.innerHTML = `<p><strong>${textInput}</strong> is a palindrome.</p>`;
    } else {
        inputResult.innerHTML = `<p><strong>${textInput}</strong> is not a palindrome.</p>`;
    }
});

