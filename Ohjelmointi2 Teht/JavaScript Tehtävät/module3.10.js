const candis = [];

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    candidates();
    displayResults(resultDisplay);
  });
});

function candidates() {
  let candidates = Number(prompt("How many candidates:"))
  for(let i = 1; i <= candidates; i++){
    let names = prompt("Give candidate name: Candidate"+ i);
    candis.push({
    name: names,
    votes: 0
    });
  }
  let voters = Number(prompt("How many voters:"))
  for(let i = 1; i <= voters; i++){
    let votedFor = prompt("Voter"+ 1 +"name");
    const candidateMatch = candis.find(c => c.name.toLowerCase() === votedFor.toLowerCase().trim());
    if (candidateMatch) {
      candidateMatch.votes++;
    } else {
      alert(`Candidate "${votedFor}" not found. This vote is invalid!`);
    }
  }
}
  

function displayResults(displayElement) {
  let outputHtml = "<h3>Election Results:</h3><ul>";
  
  candis.forEach(candidate => {
    outputHtml += `<li>${candidate.name}: ${candidate.votes} votes</li>`;
  });
  
  outputHtml += "</ul>";
  displayElement.innerHTML = outputHtml;
}