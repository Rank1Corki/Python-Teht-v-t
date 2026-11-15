document.addEventListener("DOMContentLoaded", () => {
  const paragraph = document.getElementById("trigger");
  const image = document.getElementById("target");

  paragraph.addEventListener("mouseover", () => {
    image.src = "img/picB.jpg";
  });

  paragraph.addEventListener("mouseout", () => {
    image.src = "img/picA.jpg";
  });
});
