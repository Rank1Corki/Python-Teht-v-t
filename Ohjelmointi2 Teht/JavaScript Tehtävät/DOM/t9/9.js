document.addEventListener("DOMContentLoaded", () => {
  const calculate = document.getElementById("start");
  const displayResults = document.getElementById("result");

  let numinput = document.getElementById("calculation");


  calculate.addEventListener("click", () => {
    const input = numinput.value; 
    let answr;
    if (input.includes("+")) {
    const parts = input.split("+") 
    answr = Number(parts[0]) + Number(parts[1])
    } else if (input.includes("-")) {
    const parts = input.split("-") 
    answr = Number(parts[0]) - Number(parts[1])
    } else if (input.includes("*")){
    const parts = input.split("*") 
    answr = Number(parts[0]) * Number(parts[1])
    } else if (input.includes("/")){
    const parts = input.split("/")  
    answr = Number(parts[0]) / Number(parts[1])
    }

    displayResults.textContent = answr;
  });
});

