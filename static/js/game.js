document.addEventListener("DOMContentLoaded", () => {
  const gameInfo = document.getElementById("gameInfo");
  const starsContainer = document.getElementById("stars");

  // Animate game info
  setTimeout(() => gameInfo.classList.remove("hidden"), 500);

  // Floating stars
  for (let i = 0; i < 80; i++) {
    const star = document.createElement("div");
    star.classList.add("star");
    const size = Math.random() * 3 + 1;
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;
    star.style.left = `${Math.random() * 100}vw`;
    star.style.animationDuration = `${Math.random() * 5 + 5}s`;
    star.style.animationDelay = `${Math.random() * 5}s`;
    starsContainer.appendChild(star);
  }

  const startButton = document.getElementById("startRound");
  startButton.addEventListener("click", () => {
    alert("Round 1 will start! Solve your first puzzle 🧩");
  });
});
