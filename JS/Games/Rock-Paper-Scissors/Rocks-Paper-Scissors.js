<script>
const hide = document.getElementById("hide")
const player = document.getElementById("player")
const playerChoice = document.getElementById("playerChoice")
let result = document.getElementById("result")
const computer = document.getElementById("computer")
let computerChoiceDisplay = document.getElementById("computerChoiceDisplay")
let computerChoices
choices = document.querySelectorAll(".rock, .paper, .scissors")

const win = () => {
        hide.className = "win"
        choices.forEach((choice) => {
            choice.style.visibility = "hidden"
    })
}

const generateResponse = () => {

        let computerChoice = Math.floor(Math.random() * 3) + 1

        if (computerChoice === 1) {
                computerChoiceDisplay.innerHTML = "rock"
                console.log(computerChoice)

        }
        if (computerChoice === 2) {
                computerChoiceDisplay.innerHTML = "scissors"
                console.log(computerChoice)

        }
        if (computerChoice === 3) {
                computerChoiceDisplay.innerHTML = "paper"
                console.log(computerChoice)

        }
        
        if (computerChoiceDisplay.innerHTML == playerChoice.innerHTML){
                result.innerHTML = "Draw"
        }
        if (computerChoiceDisplay.innerHTML == "paper" & playerChoice.innerHTML == "scissors" || computerChoiceDisplay.innerHTML == "scissors" & playerChoice.innerHTML == "rock" || computerChoiceDisplay.innerHTML == "rock" & playerChoice.innerHTML == "paper"){
                result.innerHTML = "Win"
                win()
        }
        if (computerChoiceDisplay.innerHTML == "scissors" & playerChoice.innerHTML == "paper" || computerChoiceDisplay.innerHTML == "paper" & playerChoice.innerHTML == "rock" || computerChoiceDisplay.innerHTML == "rock" & playerChoice.innerHTML == "scissors"){
                result.innerHTML = "Lose"
        }
}

choices.forEach((choice) => {
        choice.addEventListener("click", () => {
                playerChoice.innerHTML = choice.innerHTML
                generateResponse()
        })
})


</script>
