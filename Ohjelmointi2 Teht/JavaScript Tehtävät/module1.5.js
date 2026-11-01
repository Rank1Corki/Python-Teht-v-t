document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton");
    const resultDisplay = document.getElementById("resultDisplay"); 

    button.addEventListener("click", () => {
        const input = prompt("Give me a year:");

        if (input === null){
            console.log("User cancelled");
            return;
        }

        const year = Number(input);

        if (year % 400 == 0) {
            resultDisplay.textContent = `year ${input} is a leap year`;
        }
        else if (year % 100 == 0) {
            resultDisplay.textContent = `year ${input} is a leap year`;
        }
        else if (year % 4 == 0) {
            resultDisplay.textContent = `year ${input} is a leap year`;
        }
        else {
            resultDisplay.textContent = `year ${input} is not a leap year`;
        }
    });
});