let timerInterval;
let timeRemaining = 120; // 2:00 in seconds

// Skorları güncellemek için API çağrısı
async function updateScore(team, points) {
    const response = await fetch('/update_score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ team, points }),
    });

    if (response.ok) {
        console.log("Score updated successfully");
    } else {
        console.error("Failed to update score");
    }
}

// Zamanlayıcıyı başlatma
function startTimer() {
    if (timerInterval) return; // Eğer zaten çalışıyorsa tekrar başlatma

    timerInterval = setInterval(() => {
        if (timeRemaining > 0) {
            timeRemaining--;
            updateTimerDisplay();
        } else {
            stopTimer();
        }
    }, 1000);
}

// Zamanlayıcıyı durdurma
function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
}

// Zamanlayıcıyı sıfırlama
function resetTimer() {
    stopTimer();
    timeRemaining = 120; // 2:00 in seconds
    updateTimerDisplay();
}

// Zamanlayıcıyı görüntüleme
function updateTimerDisplay() {
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    document.getElementById('timer-display').textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}
