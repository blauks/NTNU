$(document).ready(documentReady());

let backgroundColours = ["#fa8072", "#f5f5dc", "#a52a2a", "#fff8dc", "#5f9ea0", "#f8f8ff", "#fffff0"];
let currentColour = backgroundColours[0];

let canvasColourI = 0;
let svgColourI = 0;

function draw(mod, backgroundColour) {
    let canvas = document.getElementById("canvasDrawing");
    let ctx = canvas.getContext('2d');

    //Background
    ctx.fillStyle = backgroundColour;
    ctx.fillRect(0,0, 500, 500);

    //Blue triangle
    ctx.fillStyle = "aquamarine";
    ctx.beginPath();
    ctx.moveTo(0, 500);
    ctx.lineTo(250, 500);
    ctx.lineTo(125, 150);
    ctx.fill();

    //Tomato coloured figure
    ctx.fillStyle = "tomato";
    ctx.beginPath();
    ctx.moveTo(200, 75);
    ctx.lineTo(350, 0);
    ctx.lineTo(500, 0);
    ctx.lineTo(500, 150);
    ctx.fill();

    //Skyblue coloured figure
    ctx.fillStyle = "skyblue";
    ctx.beginPath();
    ctx.moveTo(500, 500);
    ctx.lineTo(500, 400);
    ctx.lineTo(200, 160);
    ctx.lineTo(400, 500);
    ctx.fill();

    //Circle
    ctx.fillStyle = "hotpink";
    ctx.beginPath();
    ctx.arc(135, 100, 30, 0, Math.PI * 2, true);
    ctx.fill();

    //Smiley face
    ctx.strokeStyle = "black";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(20.5, 50.5);
    ctx.lineTo(20.5,70.5);
    ctx.stroke();
    ctx.moveTo(40.5, 50.5);
    ctx.lineTo(40.5,70.5);
    ctx.stroke();
    ctx.moveTo(10.5, 80.5 + mod);
    ctx.lineTo(20.5, 90.5 - mod);
    ctx.lineTo(40.5, 90.5 - mod);
    ctx.lineTo(50.5, 80.5 + mod);
    ctx.stroke();
}

function documentReady() {
    $(".documentationButton").click(function () { 
        $(".documentation").toggle()
        $(".documentationButton").text(
            $(".documentation").is(":visible")  ? "Hide documentation" : "Show documentation"
        );
    });
    
    $("#svgDrawing").hover(changeMoodOfSVGThanos);
    $("#canvasDrawing").hover(changeMoodOfCanvasThanos);

    $("#canvasDrawing").click(function (e) { changeBackgroundColourCanvas(e) });
    $("#svgBackground").click(changeSvgBackground) 
}  

function changeMoodOfSVGThanos() {
    if($("#svgDrawing").is(":hover")){
        $(".smile").hide();
        $(".frown").show();
    }
    else {
        $(".smile").show();
        $(".frown").hide();
    }
}

function changeMoodOfCanvasThanos() {
    if($("#canvasDrawing").is(":hover")){
        draw(10, currentColour);
    }
    else {
        draw(0, currentColour);
    }
}

function changeBackgroundColourCanvas(e) {
    let x = e.pageX - $('#canvasDrawing').offset().left
    let y = Math.floor(e.pageY - $('#canvasDrawing').offset().top)
    let colourData = document.getElementById("canvasDrawing").getContext('2d').getImageData(x, y, 1, 1).data
    let pixelHexColour = "#"+colourData[0].toString(16)+colourData[1].toString(16)+colourData[2].toString(16)

    //Checks if the pixel that is pressed is the same as the background colour, and if it is the background colour changes
    //This is to make it so that you must press the background to change its colour
    if(pixelHexColour === currentColour) {
        canvasColourI = canvasColourI === 6 ? 0 : canvasColourI + 1
        currentColour = backgroundColours[canvasColourI];
        draw(10, currentColour);
    }
}

function changeSvgBackground() {    
    svgColourI = svgColourI === 6 ? 0 : svgColourI + 1
    $("#svgBackground").attr("style", "fill: " + backgroundColours[svgColourI])
}