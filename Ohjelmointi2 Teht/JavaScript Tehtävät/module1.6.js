
document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton"); 
    const resultDisplay = document.getElementById("resultDisplay"); 


    button.addEventListener("click", () => { 
        const userConfirmed = confirm("Should i calculate the square root:"); 
        if (userConfirmed) {
            let input = prompt("Give me a number"); 
    
            if (input !== null && input !== "") {
                let result = Math.sqrt(Number(input));
                resultDisplay.textContent = `The square root of ${input} is ${result}`; 
            }
        }
    });
});