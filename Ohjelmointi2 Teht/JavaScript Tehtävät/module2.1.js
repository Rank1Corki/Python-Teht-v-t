document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    let inputValue = Number(prompt("Give me a number and I'll tell you if it's a prime number:"));
    
    
    if (isNaN(inputValue) || inputValue <= 1) {
      resultDisplay.textContent = `${inputValue} is not a prime number.`;
      return;
    }

    let isPrime = true;
    
    for (let i = 2; i <= Math.sqrt(inputValue); i++) {
      if (inputValue % i === 0) {
        isPrime = false;
        break; 
      }
    }

    resultDisplay.textContent = `${inputValue} is ${isPrime ? "a prime" : "not a prime"} number.`;
  });
});