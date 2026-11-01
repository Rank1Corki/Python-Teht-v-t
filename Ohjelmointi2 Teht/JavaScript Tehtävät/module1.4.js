document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton");
    const resultDisplay = document.getElementById("resultDisplay"); 

    button.addEventListener("click", () => {
        const input = prompt("Give your name and get sorted into a class:");

        if (input === null){
            console.log("User cancelled");
            return;
        }

        const classes = ["gryffindor", "slytherin", "hufflepuff", "ravenclaw"];
        
        const randomIndex = Math.floor(Math.random() * classes.length); 
        const assignedClass = classes[randomIndex];
        
        resultDisplay.textContent = `${input}, your class is ${assignedClass}`;
    });
});