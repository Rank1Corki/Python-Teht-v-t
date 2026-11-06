const participants = []

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    resultDisplay.innerHTML = ""; 

    let inputValue = Number(prompt("Kuinka monta"));
    for(let i = 1 ; i <= inputValue; i++){
      let nimi = prompt("Give me the names of the participants"+ i );
      participants.push(nimi)
    }

    const ol = document.createElement("ol");

    for (let nimi of participants) {
      const li = document.createElement("li");
      li.textContent = nimi;
      ol.appendChild(li);
    }

    resultDisplay.appendChild(ol);
  });
});
