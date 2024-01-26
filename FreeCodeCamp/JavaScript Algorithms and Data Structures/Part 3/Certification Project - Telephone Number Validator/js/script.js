const userInput = document.getElementById("user-input");
const resultsDiv = document.getElementById("results-div");
const checkBtn = document.getElementById("check-btn");
const clearBtn = document.getElementById("clear-btn");
const numberRegex =
    /^(?:1\s?)?(?:\()?(\d\d\d\)?)(?:\s|-)?(\d\d\d)(?:\s|-)?(\d\d\d\d)$/;
const leftBracketRegex = /\(/;
const rightBracketRegex = /\)/;

checkBtn.addEventListener("click", () => {
    // 5.When you click on the #check-btn element without entering a value into the #user-input element, an alert should appear with the text Please provide a phone number
    if (userInput.value === "") {
        alert("Please provide a phone number");
        return;
    } else if (
        (leftBracketRegex.test(userInput.value) &&
            !rightBracketRegex.test(userInput.value)) ||
        (!leftBracketRegex.test(userInput.value) &&
            rightBracketRegex.test(userInput.value))
    ) {
        resultsDiv.innerHTML = `<p class="result" style="color: #471009">Invalid US number: ${userInput.value}</p>`;
    } else if (numberRegex.test(userInput.value)) {
        resultsDiv.innerHTML = `<p class="result" style="color: #23662c">Valid US number: ${userInput.value}</p>`;
    } else if (!numberRegex.test(userInput.value)) {
        resultsDiv.innerHTML = `<p class="result" style="color: #471009">Invalid US number: ${userInput.value}</p>`;
    }
});

// 6.When you click on the #clear-btn element, the content within the #results-div element should be removed
clearBtn.addEventListener("click", () => {
    resultsDiv.innerHTML = "";
});

/*
7.When the #user-input element contains 1 555-555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 1 555-555-5555.
8.When the #user-input element contains 1 (555) 555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 1 (555) 555-5555.
9.When the #user-input element contains 5555555555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 5555555555.
10.When the #user-input element contains 555-555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 555-555-5555.
11.When the #user-input element contains (555)555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: (555)555-5555.
12.When the #user-input element contains 1(555)555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 1(555)555-5555.
13.When the #user-input element contains 555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 555-5555.
14.When the #user-input element contains 5555555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 5555555.
15.When the #user-input element contains 1 555)555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 1 555)555-5555.
16.When the #user-input element contains 1 555 555 5555 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 1 555 555 5555.
17.When the #user-input element contains 1 456 789 4444 and the #check-btn element is clicked, the #results-div element should contain the text Valid US number: 1 456 789 4444.
18.When #user-input contains 123**&!!asdf# and #check-btn is clicked, #results-div should contain the text Invalid US number: 123**&!!asdf#.
19.When the #user-input element contains 55555555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 55555555.
20.When the #user-input element contains (6054756961) and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: (6054756961).
21.When the #user-input element contains 2 (757) 622-7382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 2 (757) 622-7382.
22.When the #user-input element contains 0 (757) 622-7382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 0 (757) 622-7382.
23.When the #user-input element contains -1 (757) 622-7382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: -1 (757) 622-7382.
24.When the #user-input element contains 2 757 622-7382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 2 757 622-7382.
25.When the #user-input element contains 10 (757) 622-7382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 10 (757) 622-7382.
26.When the #user-input element contains 27576227382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 27576227382.
27.When the #user-input element contains (275)76227382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: (275)76227382.
28.When the #user-input element contains 2(757)6227382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 2(757)6227382.
29.When the #user-input element contains 2(757)622-7382 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 2(757)622-7382.
30.When the #user-input element contains 555)-555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 555)-555-5555.
31.When the #user-input element contains (555-555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: (555-555-5555.
32.When #user-input contains (555)5(55?)-5555 and #check-btn is clicked, #results-div should contain the text Invalid US number: (555)5(55?)-5555.
33.When the #user-input element contains 55 55-55-555-5 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 55 55-55-555-5.
34.When the #user-input element contains 11 555-555-5555 and the #check-btn element is clicked, the #results-div element should contain the text Invalid US number: 11 555-555-5555.
*/
