"use strict";

const name = "Frank";
document.querySelector("#target").innerHTML = "Good morning, " + name + "!";



document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("promptButton");

    button.addEventListener("click", () => {
        const userName = prompt("Please enter your name:");
        console.log(userName);
        alert(`Hello, ${userName}!`);
    });
});