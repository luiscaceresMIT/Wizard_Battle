document.addEventListener("DOMContentLoaded", function() {
    // Check if we are on the battle page
    if (document.querySelector('h1').innerText === 'Battle Round') {
        initiateBattle();
    }
});

function initiateBattle() {
    const battleButton = document.createElement('button');
    battleButton.innerText = "Start Battle";
    battleButton.addEventListener('click', performBattle);
    document.body.appendChild(battleButton);
}

function performBattle() {
    const outcomes = ["win", "lose", "draw"];
    const randomOutcome = outcomes[Math.floor(Math.random() * outcomes.length)];

    let resultMessage = "";

    switch(randomOutcome) {
        case "win":
            resultMessage = "Congratulations! You won this round.";
            break;
        case "lose":
            resultMessage = "Sorry, you lost this round. Better luck next time!";
            break;
        case "draw":
            resultMessage = "It's a draw! Both warriors are equally matched.";
            break;
    }

    displayBattleResult(resultMessage);
}

function displayBattleResult(message) {
    const resultDiv = document.createElement('div');
    resultDiv.className = "battle-result";
    resultDiv.innerText = message;
    document.body.appendChild(resultDiv);
}
