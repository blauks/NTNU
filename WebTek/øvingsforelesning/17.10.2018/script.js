const button = document.querySelector("#mybutton");
const target = document.querySelector(".target");

button.addEventListener("click", function (event){
    event.preventDefault(); 
    target.style.backgroundColor = "red";
});

countries = ["Norge", "Sverige", "Danmark", "Spania"]

for (country of countries){
    console.log(country)
}

const newArray = countries.map(country => country.toUpperCase());
const otherArray = countries.filter(x => doOtherThing(x))

const anotherArray = [];

for (country of countries){
    anotherArray.push(country.toUpperCase())
}

console.log(countries)
console.log(newArray)
console.log(otherArray)
console.log(anotherArray)

function doOtherThing(country){
    if(country.length === 5){
        return true;
    } else {
        return false;
    }
}