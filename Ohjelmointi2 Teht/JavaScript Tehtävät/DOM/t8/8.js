document.addEventListener("DOMContentLoaded", () => {
  const calculate = document.getElementById("start");
  const displayResults = document.getElementById("result");
  const option = document.getElementById("operation");
  let num1input = document.getElementById("num1");
  let num2input = document.getElementById("num2");

  calculate.addEventListener("click", () => {
    const val1 = Number(num1input.value);
    const val2 = Number(num2input.value);
    if(option.value === "add"){
        let sum = val1 + val2;
        displayResults.textContent = sum
    }
    if(option.value === "sub"){
        let sub = val1 - val2;
        displayResults.textContent = sub
    }
    if(option.value === "multi"){
        let multi = val1 * val2;
        displayResults.textContent = multi
    }
    if(option.value === "div"){
        let div = val1 / val2;
        displayResults.textContent = div
    }
  });
});

