const numbers = [];

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    resultDisplay.innerHTML = ""; 
    numbers.length = 0;

    ask();



    const ul = document.createElement("ul");

    for (let number of numbers) {
      const li = document.createElement("li");
      li.textContent = number; 
      ul.appendChild(li);
    }
    resultDisplay.appendChild(ul);
    console.log(resultDisplay);
  });
});

function ask() {
  let dice;
  let inputValue = Number(prompt("give me the sides of the die"))
  while (dice !== inputValue) {
    dice = Math.floor(Math.random() * inputValue) + 1;
    
    numbers.push(dice);
    if(dice === inputValue){
      break;
    }
  }
}