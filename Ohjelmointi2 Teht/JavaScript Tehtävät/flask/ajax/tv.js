const form = document.querySelector('#search-form');
const input = document.querySelector('#query');

form.addEventListener('submit', async function (event) {
  event.preventDefault();

  const query = input.value.trim();
  if (!query) return;

  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`);

    const data = await response.json();
    console.log(data);

    if (Array.isArray(data)) {
      showData(data);
    } else {
      console.error('Expected an array, got:', data);
    }
  } catch (error) {
    console.error('Fetch failed:', error);
  }
});

const resultsContainer = document.querySelector(`#results`)

function showData(data){
    resultsContainer.innerHTML = "";

    for(const item of data){
        const show = item.show;
        
        const article = document.createElement("article");
        
        const title = document.createElement("h2");
        title.textContent = show.name;

        const link = document.createElement("a");
        link.href = show.url;
        link.target = "_blank"
        link.textContent = "View on tvmaze";

        const img = document.createElement("img");
        img.src = show.image ? show.image.medium : "https://placehold.co/210x295?text=Not%20Found";
        img.alt = show.name;

        const summary = document.createElement('div');
        summary.innerHTML = show.summary;

        article.append(title, img, summary, link);
        resultsContainer.appendChild(article);
    }
}