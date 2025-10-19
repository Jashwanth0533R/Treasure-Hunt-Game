document.addEventListener("DOMContentLoaded", () => {
  const startButton = document.getElementById("startRound");
  const questionBox = document.getElementById("questionBox");
  const playerAge = document.getElementById("playerAge").textContent;
  const currentKeysDisplay = document.getElementById("currentKeys");

  let currentQuestionId = null;

  async function fetchNewQuestion() {
      startButton.disabled = true;
      startButton.textContent = 'Loading...';

      try {
        const res = await fetch("/get_question", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ age: playerAge })
        });

        const data = await res.json();
        currentQuestionId = data.id;

        if (!data.id) {
            questionBox.innerHTML = `<p class="result-message error">${data.question}</p>`;
            startButton.textContent = 'Try Again';
        } else {
            const optionsArray = data.options ? data.options.split(',').map(opt => opt.trim()).filter(opt => opt.length > 0) : [];
            let optionsHTML = '';

            if (optionsArray.length > 0) {
                // Create multiple-choice buttons
                optionsHTML = optionsArray.map(option => 
                    `<button class="option-btn" data-answer="${option.toLowerCase()}">${option}</button>`
                ).join('');
                
            } else {
                // Fallback to text input
                optionsHTML = `<input type="text" id="answerInput" placeholder="Type your answer here">
                               <button id="submitTextAnswer">Submit Answer 🔑</button>`;
            }

            questionBox.innerHTML = `
              <h3>🧩 Your Challenge:</h3>
              <p>${data.question}</p>
              <div id="optionsContainer">${optionsHTML}</div>
            `;
            
            // Attach listeners to buttons
            if (optionsArray.length > 0) {
                document.querySelectorAll('.option-btn').forEach(button => {
                    button.addEventListener('click', handleOptionClick);
                });
            } else {
                 document.getElementById("submitTextAnswer").addEventListener("click", handleSubmitAnswer);
            }

            startButton.style.display = 'none'; 
        }

      } catch (err) {
        console.error("Error fetching question:", err);
        questionBox.innerHTML = `<p class="result-message error">Connection error. Check console/server.</p>`;
        startButton.textContent = 'Start Challenge';
      }

      startButton.disabled = false;
  }
  
  startButton.addEventListener("click", fetchNewQuestion);

  function handleOptionClick(event) {
    const userAnswer = event.target.dataset.answer;
    handleSubmitAnswer(userAnswer, event.target);
  }

  async function handleSubmitAnswer(mcqAnswer = null, clickedButton = null) {
    let userAnswer;
    let submissionButton;
    const isMCQ = !!mcqAnswer;

    if (isMCQ) {
        userAnswer = mcqAnswer;
        submissionButton = clickedButton;
        document.querySelectorAll('.option-btn').forEach(btn => btn.disabled = true); 
    } else {
        const answerInput = document.getElementById("answerInput");
        submissionButton = document.getElementById("submitTextAnswer");
        userAnswer = answerInput.value.trim();

        if (userAnswer === "") {
          alert("Please type an answer!");
          return;
        }
    }

    submissionButton.disabled = true;
    submissionButton.textContent = 'Checking...';

    try {
      const res = await fetch("/submit_answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: currentQuestionId, answer: userAnswer }) 
      });

      const data = await res.json();
      
      // Update key display immediately with an animation class
      const oldKeys = parseInt(currentKeysDisplay.textContent);
      const keyDiff = data.new_keys - oldKeys;
      
      currentKeysDisplay.classList.add('animate-change'); // Trigger CSS animation
      currentKeysDisplay.textContent = data.new_keys;
      
      // Highlight the correct/incorrect option button
      if (isMCQ) {
        if (data.correct) {
            submissionButton.classList.add('correct');
        } else {
            submissionButton.classList.add('incorrect');
        }
      }

      // Show dynamic result message
      questionBox.innerHTML = `
        <h3 class="${data.correct ? 'correct' : 'incorrect'}">Challenge Result:</h3>
        <p class="result-message ${data.correct ? 'correct' : 'incorrect'}">
          ${data.message}
        </p>
        <p class="key-change-feedback">+${keyDiff} Keys!</p>
        <p>Redirecting to the map...</p>
      `;
      
      // REDIRECT TO MAP after animation delay
      setTimeout(() => {
          window.location.href = data.redirect;
      }, 2500); // Increased delay for better visual effect
      
    } catch (err) {
      console.error("Error submitting answer:", err);
      // Reset state on failure
      if (submissionButton) submissionButton.textContent = 'Submit Answer 🔑';
      questionBox.innerHTML += `<p class="result-message error">Connection error. Try again.</p>`;
    }
  }
  
  // Start the first round automatically when the page loads
  startButton.click();
});
