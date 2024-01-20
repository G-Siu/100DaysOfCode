function cleanInputString(str) {
    // As \W implicitly includes '_', regex must be written out in full
    const regex = /[^A-Za-z0-9]/g;
    return str.replace(regex, "");
}

const checkBtn = document.getElementById("check-btn");

// Function for when button is clicked
checkBtn.addEventListener("click", () => { 
    // Get user input
    const textInput = document.getElementById("text-input").value;
    // 4. When you click on the #check-btn element without entering a value into the #text-input element, an alert should appear with the text Please input a value
    if (textInput == null || textInput == "") {
        alert("Please input a value")
    } else {
        // Use function to clean up any non-alphanumeric character
        const cleanInput = cleanInputString(textInput).toLowerCase();
        // Reverse the input
        const reverseInput = cleanInput.split("").reverse().join("");
        // Initialise the result div element
        const inputResult = document.getElementById("result");
        if (cleanInput === reverseInput) {
            // If palindrome, output as result
            inputResult.innerHTML = `<p><strong>${textInput}</strong> is a palindrome.</p>`;
        } else {
            // If not palindrome, output as result
            inputResult.innerHTML = `<p><strong>${textInput}</strong> is not a palindrome.</p>`;
        }
    }
    
});

/*
5. When the #text-input element only contains the letter A and the #check-btn element is clicked, the #result element should contain the text A is a palindrome ✓
6. When the #text-input element contains the text eye and the #check-btn element is clicked, the #result element should contain the text eye is a palindrome ✓
7. When the #text-input element contains the text _eye and the #check-btn element is clicked, the #result element should contain the text _eye is a palindrome ✓
8. When the #text-input element contains the text race car and the #check-btn element is clicked, the #result element should contain the text race car is a palindrome ✓
9. When the #text-input element contains the text not a palindrome and the #check-btn element is clicked, the #result element should contain the text not a palindrome is not a palindrome ✓
10. When the #test-input element contains the text A man, a plan, a canal. Panama and the #check-btn element is clicked, the #result element should contain the text A man, a plan, a canal. Panama is a palindrome ✓
11. When the #text-input element contains the text never odd or even and the #check-btn element is clicked, the #result element should contain the text never odd or even is a palindrome ✓
12. When the #text-input element contains the text nope and the #check-btn element is clicked, the #result element should contain the text nope is not a palindrome ✓
13. When the #text-input element contains the text almostomla and the #check-btn element is clicked, the #result element should contain the text almostomla is not a palindrome✓
14. When the #text-input element contains the text My age is 0, 0 si ega ym. and the #check-btn element is clicked, the #result element should contain the text My age is 0, 0 si ega ym. is a palindrome ✓
15. When the #text-input element contains the text 1 eye for of 1 eye. and the #check-btn element is clicked, the #result element should contain the text 1 eye for of 1 eye. is not a palindrome
16. When the #text-input element contains the text 0_0 (: /-\ :) 0-0 and the #check-btn element is clicked, the #result element should contain the text 0_0 (: /-\ :) 0-0 is a palindrome ✓
17. When the #text-input element contains the text five|\_/|four and the #check-btn element is clicked, the #result element should contain the text five|\_/|four is not a palindrome ✓
*/
