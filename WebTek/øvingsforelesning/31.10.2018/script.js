const canvas = document.querySelector("#myCanvas");
const ctx = canvas.getContext("2d");

//mast
ctx.rect(235,250,30,50);
ctx.fillStyle = "saddlebrown";
ctx.fill();

//seil
ctx.beginPath();
ctx.moveTo(100,250);
ctx.lineTo(400,250);
ctx.lineTo(250,100);
ctx.fillStyle = "moccasin";
ctx.fill();

//båt
ctx.beginPath();
ctx.arc(250,300,175,0,Math.PI,false);
ctx.fillStyle="darkkhaki";
ctx.fill();     

const countries = ['Norway', 'Sweden', 'Denmark', 'New Zealand'];
const countriesStartingWithN = countries.filter(function(x) {
       return x.startsWith("N");
})
console.log(countries)
console.log(countriesStartingWithN)