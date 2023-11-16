const quotes = [
  "Things are only impossible until they are not",
  "It is possible to commit no errors and still lose. That is not a weakness. That is life",
  "There is a way out of every box, a solution to every puzzle; it is just a matter of finding it",
  "Without freedom of choice there is no creativity",
  "Logic is the beginning of wisdom, not the end",
  "Improve a mechanical device and you may double productivity, but improve yourself and you gain a thousandfold"
]

const quote = document.getElementById("quote");
const input = document.getElementById("typedValue");
const start = document.getElementById("button");
const message = document.getElementById("message");

let wordQueue, highlightPosition, startTime;

function startGame() {
  console.log("Game started!");
  
  const quoteIndex = Math.floor(Math.random() * quotes.length);  // floor rounds the random number to get index number for number of quotes in array
  const quoteText = quotes[quoteIndex];
  
  wordQueue = quoteText.split(" ");

  quote.innerHTML = wordQueue.map((word) => `<span>${word}</span>`).join("");
  highlightPosition = 0;
  quote.childNodes[highlightPosition].className = "highlight";
  
  startTime = new Date().getTime();  // Gets current time in ms since epoch
  
  start.className = "started";
  document.body.className = "";
}

function checkInput() {
  const currentWord = wordQueue[0].replaceAll(".", "").replaceAll(",", "").replaceAll(";", "");  // Replace punctuation with nothing for game flow (optional)
  const typedValue = input.value.trim();

  if (currentWord !== typedValue) {
    input.className = currentWord.startsWith(typedValue) ? "" : "error";
    return;
  }
  wordQueue.shift(); // shift removes the first item in the array (the 0th element)
  input.value = ""; // empty the text input

  quote.childNodes[highlightPosition].className = "";
  highlightPosition++;

  if (wordQueue.length === 0) {
    gameOver();
    return;
  }
  quote.childNodes[highlightPosition].className = "highlight";
}

function gameOver() {
  const elapsedTime = new Date().getTime() - startTime;
  
  message.innerHTML = `
  <span class="congrats">Congratulations!</span>
  <br>
  You finished in ${elapsedTime / 1000} seconds.
  `
  
  document.body.className = "winner";
}

start.addEventListener("click", startGame);
input.addEventListener("input", checkInput);
