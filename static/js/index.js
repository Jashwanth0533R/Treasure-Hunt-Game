document.addEventListener("DOMContentLoaded", () => {
  const startBtn = document.getElementById("startBtn");
  const chest = document.getElementById("chest");

  startBtn.addEventListener("click", (ev) => {
    ev.preventDefault();
    const nameInput = document.getElementById("name");
    const ageInput = document.getElementById("age");

    const name = nameInput.value.trim();
    const age = ageInput.value.trim();

    if (!name || !age || parseInt(age) < 5) {
      alert("Please enter a valid name and age (5+).");
      return;
    }

    // Disable inputs/button
    nameInput.disabled = true;
    ageInput.disabled = true;
    startBtn.disabled = true;

    // Simulate chest opening and redirect
    chest.classList.add('open');

    // After a short animation delay, redirect to /game
    setTimeout(() => {
      const url = `/game?name=${encodeURIComponent(name)}&age=${encodeURIComponent(age)}`;
      window.location.href = url;
    }, 1000); 
  });
});
