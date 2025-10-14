document.addEventListener("DOMContentLoaded", () => {
  const startInfo = document.getElementById("startInfo");
  const startButton = document.getElementById("startAdventure");
  const starsContainer = document.getElementById("stars");

  // Fade in the start box
  setTimeout(() => startInfo.classList.remove("hidden"), 400);

  // Create floating stars
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

  startButton.addEventListener("click", () => {
    const name = document.getElementById("name").value.trim();
    const age = document.getElementById("age").value.trim();
    if (!name || !age) {
      alert("Enter your name and age first!");
      return;
    }
    alert(`🎉 Congrats ${name}! You got 10 bonus keys! 🗝️`);
    window.location.href = `/game?name=${encodeURIComponent(name)}&age=${encodeURIComponent(age)}`;
  });
});
