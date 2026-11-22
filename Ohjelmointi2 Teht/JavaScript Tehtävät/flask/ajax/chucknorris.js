
const resultsContainer = document.querySelector("#results");

const form = document.querySelector('#search-form');
const input = document.querySelector('#query');

form.addEventListener('submit', async function (event) {
  event.preventDefault();

  const query = input.value.trim();
  if (!query) return;

  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(query)}`);

    const data = await response.json();
    console.log(data);

    if (Array.isArray(data.result)) {
      showData(data.result);
    } else {
      console.error('Expected an array, got:', data);
    }
  } catch (error) {
    console.error('Fetch failed:', error);
  }
});

function showData(jokes) {
  resultsContainer.innerHTML = "";

  if (jokes.length === 0) {
    resultsContainer.textContent = "No jokes found.";
    return;
  }

  for (const joke of jokes) {
    const article = document.createElement("article");

    const paragraph = document.createElement("p");
    paragraph.textContent = joke.value;

    article.append(paragraph);
    resultsContainer.appendChild(article);
  }
}