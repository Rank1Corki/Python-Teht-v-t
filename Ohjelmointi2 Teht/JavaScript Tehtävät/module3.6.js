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
  
  while (dice !== 6) {
    dice = Math.floor(Math.random() * 6) + 1;
    
    numbers.push(dice);
    if(dice === 6){
      break;
    }
  }
}