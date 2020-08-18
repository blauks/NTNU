$(document).ready(documentReady());

function draw(mod) {
    let canvas = document.getElementById("canvasDrawing");
    let ctx = canvas.getContext('2d');

    //Background
    ctx.fillStyle = "salmon";
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
    $(".documentationButton").click(showOrHideDocumentation);
    $("#svgDrawing").hover(changeMoodOfSVGThanos);
    $("#canvasDrawing").hover(changeMoodOfCanvasThanos);

}

function showOrHideDocumentation() {
    if($(".documentation").is(":visible")) {
        $(".documentation").hide();
    } else {
        $(".documentation").show();
    }
}

function changeMoodOfSVGThanos() {
    if($("#svgDrawing:hover").length != 0){
        $(".smile").hide();
        $(".frown").show();
    }
    else {
        $(".smile").show();
        $(".frown").hide();
    }
}

function changeMoodOfCanvasThanos() {
    if($("#canvasDrawing:hover").length != 0){
        draw(10);
    }
    else {
        draw(0);
    }
}

