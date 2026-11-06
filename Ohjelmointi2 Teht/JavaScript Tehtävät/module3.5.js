const numbers = [];

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    resultDisplay.innerHTML = ""; 
    numbers.length = 0;

    ask();

    numbers.sort((a,b) => a - b);

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
  let inputValue; 
  
  while (inputValue !== 0) {
    inputValue = Number(prompt("Give a number if you enter the same number this stops"));
    
    if (numbers.includes(inputValue)) {
      alert("list already has that number");
      break;
    }else{
      numbers.push(inputValue);
    }
  }
}