/*function daysUntilChristmas(){
    var christmas = new Date(2018,11,24,0,0,0,0);
    var today = new Date();
    var months = christmas.getMonth() - today.getMonth();
    return(christmas.getDate() - today.getDate() + (months*30));
}

console.log(daysUntilChristmas())

const me = JSON.parse('{"name" : "Jonathan Brooks","age" : 19,"gender" : "male","school" : "NTNU"}')

console.log(me.name)

//a = setTimeout(function(){alert("Hei")},1000);

const canvasElement = document.getElementById("myCanvas")

const ctx = canvasElement.getContext("2d");

ctx.fillstyle = "black";

ctx.beginPath()
ctx.arc(100,100,75,0,2*Math.PI,false);
ctx.stroke();
ctx.beginPath()
ctx.arc(80,80,10,0,2*Math.PI,false);
ctx.stroke();
ctx.beginPath()
ctx.arc(120,80,10,0,2*Math.PI,false);
ctx.stroke();
ctx.beginPath()
ctx.arc(100,130,30,0,Math.PI)
ctx.stroke()
ctx.closePath()

ctx.beginPath();
ctx.moveTo(40,40);
ctx.lineTo(160,90);
ctx.stroke()

ctx.beginPath()
ctx.moveTo(160,40);
ctx.lineTo(40,90);
ctx.stroke();

ctx.beginPath()
ctx.arc(100,100,60,0,Math.PI,false);
ctx.fill();
ctx.closePath();



var canvas = document.getElementById("myCanvas")
var c = canvas.getContext("2d")

c.beginPath();
c.fillstyle = "black";
c.fillRect(90,40,20,100);
c.closePath()

c.beginPath()
c.moveTo(90,40)
c.lineTo(50,130)
c.lineTo(80,120)
c.lineTo(90,40)
c.closePath()
c.fillStyle = "yellow";
c.fill()

c.beginPath()
c.moveTo(110,40)
c.lineTo(120,130)
c.lineTo(170,130)
c.lineTo(110,40)
c.closePath()
c.fill()

c.beginPath()
c.moveTo(20,140)
c.lineTo(180,140)
c.lineTo(150,170)
c.lineTo(70,170)
c.lineTo(20,140)
c.closePath()
c.fillStyle = "green";
c.fill()
c.stroke()

var canvasE = document.getElementById("myCanvas")
var c = canvasE.getContext("2d")

c.fillStyle = "blue";

c.beginPath();
c.arc(75,75,45,0,2*Math.PI)
c.stroke()

c.beginPath()
c.rect(30,10,90,130)
c.stroke()

c.beginPath()
c.moveTo(75,10)
c.lineTo(75,140)
c.stroke()

c.beginPath()
c.moveTo(30,75)
c.lineTo(120,75)
c.stroke()

var i = 0;
var parag = document.getElementById("pTest")
while(i<10){
    parag.innerHTML += "The number is " + i + "<br>"
    i++;        
}

document.write("<br>"+1)
*/

var canvas = document.getElementById("myCanvas")
var c = canvas.getContext("2d")

c.beginPath()
c.arc(70,70,50,0,2*Math.PI)
c.stroke()

c.beginPath()
c.arc(50,50,5,0,2*Math.PI)
c.stroke()

c.beginPath()
c.arc(90,50,5,0,2*Math.PI)
c.stroke()

c.beginPath()
c.arc(70,90,20,0,Math.PI)
c.stroke()