const numero = []

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    for(let i = 0; i < 5; i++){
            let inputValue = Number(prompt("Give me five numbers"));
            numero.push(inputValue);
    }
    numero.sort((a, b) => {
    console.log(a, b);
    return b - a;
    });
    resultDisplay.textContent = `List of numbers ${numero}`;
  });
});
