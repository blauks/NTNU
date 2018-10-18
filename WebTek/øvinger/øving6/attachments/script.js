const income = document.getElementById("income");
const wealth = document.getElementById("savings");

function tax(){
        let x = income.value;
        let y = wealth.value;
        document.getElementById("taxes").value = (x * 0.35) + (y * 0.25)
}