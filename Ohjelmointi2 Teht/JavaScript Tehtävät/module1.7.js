document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton"); 
    const resultDisplay = document.getElementById("resultDisplay"); 


    button.addEventListener("click", () => { 
        const dieCount = prompt("how many dice are thrown:"); 

        if (isNaN(dieCount) || dieCount <= 0) {
        resultDisplay.textContent = "Please enter a valid number of dice.";
        return;
        }

        let totalSum = 0
        
        for(let i = 0; i < dieCount; i++){
            const randomRoll = Math.floor(Math.random() * 6) + 1;   
            totalSum += randomRoll;
        }
       resultDisplay.textContent = `The sum of the dice thrown is ${totalSum}`;
    });
});