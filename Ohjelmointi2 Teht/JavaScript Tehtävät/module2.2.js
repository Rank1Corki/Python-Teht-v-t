document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("promptButton");
  const resultDisplay = document.getElementById("resultDisplay");

  button.addEventListener("click", () => {
    let inputValue = Number(prompt("How many dice do u need me to calculate"));
    let summa = Number(prompt("Give the sum of the dice u want it to be"))
    
    const result = getDiceSumProbability  (inputValue, summa);
    resultDisplay.textContent = `U have a: ${result} chance of getting ${summa} as your sum.`;
  });
});
function getDiceSumProbability(numDice, targetSum, sides = 6) {
    const totalOutcomes = Math.pow(sides, numDice);
    let dp = new Array(targetSum + 1).fill(0);
    dp[0] = 1;

    for (let d = 0; d < numDice; d++) {
        let nextDp = new Array(targetSum + 1).fill(0);
        for (let currentSum = 0; currentSum <= targetSum; currentSum++) {
            if (dp[currentSum] === 0) continue;
            for (let face = 1; face <= sides; face++) {
                if (currentSum + face <= targetSum) {
                    nextDp[currentSum + face] += dp[currentSum];
                }
            }
        }
        dp = nextDp;
    }

    const probability = dp[targetSum] / totalOutcomes;
    return (probability * 100).toFixed(2) + "%";
}



