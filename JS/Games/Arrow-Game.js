<script>
const boardWidth = 1250
const boardHeight = 400
const hide = document.getElementById("hide")
const board = document.getElementById("board")
let run = true

const win = () => {
        let run = false
        hide.className = "win"
        window.location.href = "{% url "game" %}"
}
const lose = () => {
    let run = false
    window.location.href = "{% url "game" %}"
}

if (run==true) {
        class Cible {
        constructor(xAxis, yAxis) {
            this.bottomLeft = [xAxis, yAxis]
            this.bottomRight = [xAxis + 60, yAxis]
            this.topLeft = [xAxis, yAxis + 60]
            this.topRight = [xAxis + 60, yAxis + 60]
        }
    }

    function randomIntFromInterval(min, max) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min);
    }

    const cibles = []

    for (let i = 0; i<20; i++) {
        cibles.push(new Cible(randomIntFromInterval(50, 1100), randomIntFromInterval(100, 350)))
    }

    let num_cible_touched = 0
    let temps = 10

    function addCible() {
        if (num_cible_touched == 20) {
            win()
        }
        else {
            const cible = document.createElement("div")
            cible.className = "cible"
            cible.style.left = cibles[num_cible_touched].bottomLeft[0] + "px"
            cible.style.bottom = cibles[num_cible_touched].bottomLeft[1] + "px"
            board.appendChild(cible)
            const cibles_special = document.querySelectorAll("div")
            cibles_special.forEach((cible_special) => {
                cible_special.addEventListener("click", () => {
                    cible_special.remove()
                    num_cible_touched++
                    let temps = 1000
                    addCible()
            })
            })
        }
    }

    addCible()

    const sleep = (ms) => new Promise(r => setTimeout(r, ms));

    async function demo() {
        for (let i = 0; i < temps; i++) {
            console.log(`Waiting ${i} seconds...`, temps);
            await sleep(i * 1000);
        }
        lose()
    }
    demo()

}
</script>
