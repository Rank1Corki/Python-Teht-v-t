document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("source");
  const displayResults = document.getElementById("target");
  const input1 = document.querySelector('input[name="firstname"]');
  const input2 = document.querySelector('input[name="lastname"]');

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const firstname = input1.value;
    const lastname = input2.value;
    displayResults.textContent = `Your name is ${firstname} ${lastname}`;
  });
});