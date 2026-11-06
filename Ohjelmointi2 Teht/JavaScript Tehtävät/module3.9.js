const oglist = [];
const newlist = [];

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById('container');
  const resultDisplay = document.getElementById("resultDisplay");

  const inputField = document.createElement("input");
  inputField.type = 'text';                  
  inputField.placeholder = 'Type here...';    
  container.appendChild(inputField);
  
  const addButton = document.createElement("button");
  addButton.textContent = "Add to List";
  addButton.style.marginLeft = "10px"; 
  container.appendChild(addButton);

  addButton.addEventListener('click', () => {
    handleEvenNumber(inputField.value);

    resultDisplay.innerHTML = `Original list: [${oglist.join(', ')}]<br>Even list: [${newlist.join(', ')}]`;

    inputField.value = '';
    inputField.focus(); 
  });
});

function handleEvenNumber(inputValue) {
  if (inputValue.trim() === '') return; 
  
  const number = Number(inputValue);
  if (!isNaN(number)) {
    oglist.push(number);
    if (number % 2 === 0) {
      newlist.push(number);
    }
  }
}