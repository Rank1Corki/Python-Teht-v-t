const list = document.createElement("li");
const text = document.createTextNode("Second item");

list.appendChild(text);
document.getElementById("my-item").appendChild(list);
