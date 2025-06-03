let taps = 0;
let logs = 0;
let energy = 100;
const maxEnergy = 100;

const tapsDisplay = document.getElementById("taps");
const logsDisplay = document.getElementById("logs");
const energyDisplay = document.getElementById("energy");
const tapBtn = document.getElementById("tapBtn");

function updateUI() {
  tapsDisplay.textContent = taps;
  logsDisplay.textContent = logs;
  energyDisplay.textContent = energy;
}

function restoreEnergy() {
  if (energy < maxEnergy) {
    energy += 1;
    if (energy > maxEnergy) energy = maxEnergy;
    updateUI();
  }
}

// каждую секунду восстанавливаем энергию
setInterval(restoreEnergy, 1000);

tapBtn.addEventListener("click", () => {
  if (energy > 0) {
    taps += 1;
    energy -= 1;
    if (taps % 100 === 0) {
      logs += 1; // каждые 100 тапов — полено
    }
    updateUI();
  }
});

updateUI();
