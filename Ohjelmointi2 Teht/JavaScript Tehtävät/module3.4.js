const numbers = [];

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    resultDisplay.innerHTML = ""; 
    numbers.length = 0;

    ask();

    numbers.sort((a, b) => a - b).reverse();

    const ul = document.createElement("ul");

    for (let number of numbers) {
      const li = document.createElement("li");
      li.textContent = number; 
      ul.appendChild(li);
    }
    
    resultDisplay.appendChild(ul);  
  });
});

function ask() {
  let inputValue; 
  
  while (inputValue !== 0) {
    inputValue = Number(prompt("Give a number (Enter 0 to stop):"));
    
    if (inputValue !== 0 && !isNaN(inputValue)) {
      numbers.push(inputValue);
    }
  }
}