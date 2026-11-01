document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton");
    const resultDisplay = document.getElementById("resultDisplay"); 

    button.addEventListener("click", () => {
        let input = prompt("Give 3 numbers separated by spaces:");

        if (input === null){
            console.log("User cancelled");
            return;
        }

        let parts = input.trim().split(/\s+/);
        

        if (parts.length === 3 && parts.every(num => num !== "" && Number.isInteger(Number(num)))) {
            let all = parts.map(num => parseInt(num, 10));
            let [first, second, third] = all;

            let summa = first + second + third;

            let keskiarvo = summa / 3; 

            resultDisplay.textContent = `Summa: ${summa}, Keskiarvo: ${keskiarvo}`;
        } else {
            alert("Invalid input! give 3 numbers seperated by spaces.");
        }
    });
});