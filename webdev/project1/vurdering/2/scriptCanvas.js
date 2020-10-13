var scirc = {
        x: 100,
        y: 200,
        radius: 30,
        rr: 30 * 30,
        color: "red",
        hover: "white"

};
var mcirc = { 
        x: 210,
        y: 260,
        radius: 75,
        rr: 75 * 75,
        color:"white",
        hover: "green",
        hoverable: false

};
var lcirc = { 
        x: 390,
        y: 295,
        radius: 100,
        rr: 100 * 100,
        color:"black",
        hover:"yellow",
        hoverable: false

};
var rtriangle = {
        x1:500,
        x2:300,
        x3:300,
        x4:500,
        y1:0,
        y2:200,
        y3:0,
        y4:0,
        color:"grey",
        hover:"purple",
        hoverable: false
}

var ltriangle = {
        x1:0,
        x2:0,
        x3:230,
        x4:0,
        y1:150,
        y2:400,
        y3:400,
        y4:150,
        color: "green",
        hover: "orange",
        hoverable: false
}
var diamond = {
        x1:50,
        x2:100,
        x3:50,
        x4:0,
        x5:50,
        y1:50,
        y2:100,
        y3:150,
        y4:100,
        y5:50,
        color: "yellow",
        hover: "black",
        hoverable: false
}
var backrect = {
        x1:0,
        y1:0,
        x2:500,
        y2:500,
        color:"blue"
}

function drawTriangle(triangle){
        ctx.beginPath();
        if(triangle.hoverable){
                ctx.fillStyle = triangle.hover;
        } else ctx.fillStyle = triangle.color;
        ctx.moveTo(triangle.x1, triangle.y1);
        ctx.lineTo(triangle.x2, triangle.y2);
        ctx.lineTo(triangle.x3, triangle.y3);
        ctx.lineTo(triangle.x4, triangle.y4);
        ctx.fill();
        ctx.closePath();
}
function triangleHover(x, y, triangle){
        ctx.beginPath();
        ctx.moveTo(triangle.x1, triangle.y1);
        ctx.lineTo(triangle.x2, triangle.y2);
        ctx.lineTo(triangle.x3, triangle.y3);
        ctx.lineTo(triangle.x4, triangle.y4);
        ctx.closePath();
        return ctx.isPointInPath(x,y)
}
function drawEllipse(color){
        ctx.beginPath();
        ctx.fillStyle = color;
        ctx.moveTo(100,100);
        ctx.ellipse(200, 100, 55, 75, Math.PI / 2, 0, 2 * Math.PI);
        ctx.fill();
        ctx.closePath();
}
function drawCircle(circle){
        ctx.beginPath();
        if(circle.hoverable){
                ctx.fillStyle = circle.hover;
        } else ctx.fillStyle = circle.color;
        ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
}
function circleHover(x, y, circle){
        ctx.beginPath();
        ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
        ctx.closePath();
        return ctx.isPointInPath(x,y)

}

function drawDiamond(diamond){
        ctx.beginPath();
        if(diamond.hoverable){
                ctx.fillStyle = diamond.hover;
        } else ctx.fillStyle = diamond.color;
        ctx.moveTo(diamond.x1,diamond.y1);
        ctx.lineTo(diamond.x2,diamond.y2);
        ctx.lineTo(diamond.x3,diamond.y3);
        ctx.lineTo(diamond.x4, diamond.y4);
        ctx.lineTo(diamond.x5,diamond.y5);
        ctx.fill();
        ctx.closePath();
}
function diamondHover(x, y, diamond){
        ctx.beginPath();
        ctx.moveTo(diamond.x1,diamond.y1);
        ctx.lineTo(diamond.x2,diamond.y2);
        ctx.lineTo(diamond.x3,diamond.y3);
        ctx.lineTo(diamond.x4, diamond.y4);
        ctx.lineTo(diamond.x5,diamond.y5);
        ctx.closePath();
        return ctx.isPointInPath(x,y)

}
function drawRect(rect){
        ctx.beginPath;
        ctx.fillStyle = rect.color;
        ctx.rect(rect.x1, rect.y1, rect.x2, rect.y2 );
        ctx.fill();
        ctx.closePath();
}

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
function drawCanvas(){
        ctx.clearRect(0,0,500,400)
        drawRect(backrect)
        drawCircle(scirc);
        drawCircle(mcirc);
        drawCircle(lcirc);
        drawEllipse("rgba(63, 206, 216, 0.473)")
        drawDiamond("yellow");
        drawTriangle(rtriangle);
        drawTriangle(ltriangle);
        drawDiamond(diamond);

}


$(document).ready(function(){
        
        $("#myCanvas").mousemove(function(e){

                x = e.pageX - $(this).offset().left;
                y = e.pageY - $(this).offset().top;
                if(diamondHover(x,y,diamond)){
                        diamond.hoverable= true;
                        drawCanvas();
                }else diamond.hoverable=false;
                 if(circleHover(x,y,scirc)){
                        scirc.hoverable= true;
                        drawCanvas();
                }else scirc.hoverable=false;
                 if(circleHover(x,y,mcirc)){
                        mcirc.hoverable=true;
                        drawCanvas();
                }else mcirc.hoverable = false;
                 if(circleHover(x,y,lcirc)){
                        lcirc.hoverable=true;
                        drawCanvas();
                }else lcirc.hoverable = false;
                 if(triangleHover(x,y,ltriangle)){
                        ltriangle.hoverable=true;
                        drawCanvas();
                }else ltriangle.hoverable = false;
                 if(triangleHover(x,y,rtriangle)){
                        rtriangle.hoverable=true;
                        drawCanvas();
                } else rtriangle.hoverable = false;
                
                drawCanvas();
        })
        // drawCanvas()
        // let shiftX = shiftY = 0;
        // $("#myCanvas").mousedown(function(e){
        //         $("#myCanvas").mousemove(function(d){
        //                 x = e.pageX - $(this).offset().left;
        //                 y = e.pageY - $(this).offset().top;
        //                 console.log("funker1")
        //                  if(circleHover(x,y,scirc)){
        //                          if(shiftX == 0 || shiftY == 0){
        //                                  shiftX = x - scirc.x;
        //                                  shiftY = y - scirc.y;
        //                          }
        //                          console.log(shiftX,shiftY);
        //                          scirc.x = (shiftX);
        //                          scirc.y = (shiftY);
                                 
        //                  }
        //                  if(circleHover(x,y,mcirc)){
        //                         let shiftX = x - mcirc.x;
        //                         let shiftY = y - mcirc.y;
                                
        //                 } if(circleHover(x,y,lcirc)){
        //                         let shiftX = x - lcirc.x;
        //                         let shiftY = y - lcirc.y;
                                
        //                 } drawCanvas()
        //         })
        //         drawCanvas();
        // }).mouseup(function(){
        //         shiftX = 0;
        //         shiftY = 0;
        // })
})

