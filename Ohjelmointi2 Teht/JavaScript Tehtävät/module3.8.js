const lista = ["Johnny", "DeeDee", "Joey", "Marky"];
let result = "";

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    concat();
  });
});

function concat() {
  for(const item of lista){
    result += item.replace(/\s/g, "");
  }
  resultDisplay.textContent = `${result}`;
}