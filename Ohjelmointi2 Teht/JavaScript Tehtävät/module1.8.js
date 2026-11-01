document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton"); 
    const resultDisplay = document.getElementById("resultDisplay"); 

    button.addEventListener("click", () => { 
        const yearstart = Number(prompt("Give me a start year")); 
        const endyear = Number(prompt("Give me an end year"));
        
        let leapyearlisthtml = `<ul>`;

        for (let year = yearstart; year <= endyear; year++){
            if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)){
                leapyearlisthtml += `<li>${year}</li>`;
            }
        }
        
        leapyearlisthtml += `</ul>`;

        resultDisplay.innerHTML = leapyearlisthtml;
    });
});