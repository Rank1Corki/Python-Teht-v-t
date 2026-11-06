const dogs = []

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    resultDisplay.innerHTML = ""; 
    dogs.length = 0;

    let inputValue = Number(prompt("how many dogs"));
    for(let i = 1 ; i <= inputValue; i++){
      let nimi = prompt("Give me the name of dog"+ i );
      dogs.push(nimi)
    }

    dogs.sort((a, b) => a.localeCompare(b)).reverse();

    const ol = document.createElement("ul");

    for (let nimi of dogs) {
      const li = document.createElement("li");
      li.textContent = nimi;
      ol.appendChild(li);
    }
    resultDisplay.appendChild(ol);  
  });
});
