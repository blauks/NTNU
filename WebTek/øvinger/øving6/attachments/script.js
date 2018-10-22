const income = document.getElementById("income");
const wealth = document.getElementById("wealth");

function taxes(){
        let x = income.value;
        let y = wealth.value;
        document.getElementById("tax").value = (x * 0.35) + (y * 0.25)
}