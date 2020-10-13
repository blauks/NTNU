$(document).ready(function(){

    //Buttons
    let svgButton = $('.svg-button');
    let canvasButton = $('.canvas-button');
    let docButton = $('.doc-button');

    //Button hover function
    const buttonHover = button => {
        button.hover(function() {
            button.css({'box-shadow': '5px 5px 2px black'});
        }, function(){
            button.css({'box-shadow' : '0px 0px 0px black'});
        });
    };

    svgButton.text('Click me!');


    buttonHover(svgButton);
    buttonHover(canvasButton);
    buttonHover(docButton);


    //Function for hide/show documentation
    docButton.click(function(){
        $('.doc-section-1').toggle();
        $('.doc-section-2').toggle();
    });



    //Declaring variables for SVG picture
    let svg = $('#svg');
    let horirect = $('#hori-rect');
    let vertrect = $('#vert-rect');
    let star = $('#star');
    let outerpoly = $('#outer-poly');
    let outercircle = $('#outer-cirlce');



    //Change color on elements when hovering
    svg.hover(function () {
        star.css('fill', '#FF00FF');
        horirect.css('fill', '#FFFFFF');
        vertrect.css('fill', '#FFFF00');
        outerpoly.css('fill', '#FF00FF');
        outercircle.css('fill', '#00FFFF');
    }, function () {
        star.css('fill', '#00FF00');
        horirect.css('fill', '#000000');
        vertrect.css('fill', '#0000FF');
        outerpoly.css('fill', '#00FF00');
        outercircle.css('fill', '#FF0000');
    });



    //SVG picture animation function
    const SVGanimation1 = () => {
        horirect.animate({width: '0', opacity: '0.5'}, 1500);
        vertrect.animate({height: '0', opacity: '0.5'}, 1500);
        outerpoly.delay(1500).fadeOut(1500);
        outercircle.delay(3000).animate({r: '0', opacity: '0.5'}, 1500);
        svgButton.text('Click again!');

    };

    //SVG picture reverse animation
    const SVGanimation2 = () => {
        outercircle.animate({r: '196', opacity: '1'}, 1500);
        outerpoly.delay(1500).fadeIn(1500);
        vertrect.delay(3000).animate({height: '362', opacity: '1'}, 1500);
        horirect.delay(3000).animate({width: '362', opacity: '1'}, 1500);
        svgButton.text('Click me!');

    };

    //Start animation on button click
    svgButton.click(function(){
        (svgButton.text() === 'Click again!') ? SVGanimation2() : SVGanimation1();
    });




    //Canvas picture setup
    const canvas = $('#canvas')[0];
    const ctx = canvas.getContext('2d');




    const blueRectangle = {
        x: 175,
        y: 69,
        width: 150,
        height: 362,
        fillStyle: "#0000FF",
    };



    const blackRectangle = {
        x: 69,
        y: 175,
        width: 362,
        height: 150,
        fillStyle: "#000000"
    };

    const redCircle = {
        xCor: 250,
        yCor: 250,
        radius: 196,
        startAngle: 0,
        endAngle: Math.PI*2,
        fillStyle: '#FF0000'
    }



    const greenOctagon = {
        xCor: [175, 325, 431, 431, 325, 175, 69, 69],
        yCor: [69, 69, 175, 325, 431, 431, 325, 175],
        fillStyle: '#00FF00'
    }

    const drawOctagon = (octagon) => {
        ctx.beginPath();
        ctx.moveTo(octagon.xCor[0], octagon.yCor[0]);
        ctx.lineTo(octagon.xCor[1], octagon.yCor[1]);
        ctx.lineTo(octagon.xCor[2], octagon.yCor[2]);
        ctx.lineTo(octagon.xCor[3], octagon.yCor[3]);
        ctx.lineTo(octagon.xCor[4], octagon.yCor[4]);
        ctx.lineTo(octagon.xCor[5], octagon.yCor[5]);
        ctx.lineTo(octagon.xCor[6], octagon.yCor[6]);
        ctx.lineTo(octagon.xCor[7], octagon.yCor[7]);
        ctx.lineTo(octagon.xCor[0], octagon.yCor[0]);
        ctx.stroke();
        ctx.fillStyle = octagon.fillStyle;
        ctx.fill();
    }

    const drawRectangle = (rectangle) => {
        ctx.fillStyle = rectangle.fillStyle;
        ctx.fillRect(rectangle.x, rectangle.y, rectangle.width, rectangle.height);
    }


    const drawCirlce = (circle) => {
        ctx.beginPath()
        ctx.arc(circle.xCor, circle.yCor, circle.radius, circle.startAngle, circle.endAngle);
        ctx.stroke();
        ctx.fillStyle = circle.fillStyle;
        ctx.fill();
    }

    const greenStar = {
        xCor: [250, 200, 325, 175, 300],
        yCor: [175, 325, 225, 225, 325],
        fillStyle: "#00FF00"
    }

    const drawStar = (poly) => {
        ctx.beginPath();
        ctx.moveTo(poly.xCor[0], poly.yCor[0]);
        ctx.lineTo(poly.xCor[1], poly.yCor[1]);
        ctx.lineTo(poly.xCor[2], poly.yCor[2]);
        ctx.lineTo(poly.xCor[3], poly.yCor[3]);
        ctx.lineTo(poly.xCor[4], poly.yCor[4]);
        ctx.lineTo(poly.xCor[0], poly.yCor[0]);
        ctx.stroke()
        ctx.fillStyle = poly.fillStyle;
        ctx.fill();
    }

    //code piece for setting up the animation (se "kilder")
    window.requestAnimFrame = ((callback) => {
        return window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.oRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            function(callback){
                window.setTimeout(callback, 1000/60);
            };
    })();

    //boolean value to check which state the picture is in
    const reverseAnimation = {
        value: false
    }

    //function for animating the canvas picture, changes the width and height of the rectangles, and the radius for the circle
    const canvasAnimation = () => {
        let speed = 7;
        redCircle.radius -= speed/2;
        drawCirlce(redCircle);
        blueRectangle.height -= speed-0.95;
        drawRectangle(blueRectangle);
        blackRectangle.width -= speed-0.95;
        drawRectangle(blackRectangle);

    }



    const animate = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        canvasAnimation();
        requestAnimFrame(() => {
            animate();
        });
    }

    //function for drawing the picture, and set the values back to before the animation
    const reset = () => {
        redCircle.radius = 196
        blueRectangle.height = 362;
        blackRectangle.width = 362;
        drawCirlce(redCircle);
        drawOctagon(greenOctagon)
        drawRectangle(blueRectangle);
        drawRectangle(blackRectangle);
        drawStar(greenStar);
    }


    //function to start the animation on button click on the canvas picture
    canvasButton.click(function(){
        if (reverseAnimation.value){
            reset();
            reverseAnimation.value = false;
            canvasButton.text('Click me!')
        } else {
            animate();
            canvasButton.text('Reset');
            reverseAnimation.value = true;
        }
    })


    reset();


    //Effect when hovering over picture
    canvas.onmouseenter = function() {
        if(!reverseAnimation.value) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            redCircle.fillStyle = '#00FFFF';
            greenOctagon.fillStyle = '#FF00FF';
            blueRectangle.fillStyle = '#FFFF00';
            blackRectangle.fillStyle = '#FFFFFF';
            greenStar.fillStyle = '#FF00FF';
            drawCirlce(redCircle);
            drawOctagon(greenOctagon);
            drawRectangle(blueRectangle);
            drawRectangle(blackRectangle);
            drawStar(greenStar);
        }
    }

    //Resets the picture to it's original colors when pointer exits the frame
    canvas.onmouseleave = function () {
        if(!reverseAnimation.value) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            redCircle.fillStyle = '#FF0000';
            greenOctagon.fillStyle = '#00FF00';
            blueRectangle.fillStyle = '#0000FF';
            blackRectangle.fillStyle = '#000000';
            greenStar.fillStyle = '#00FF00';
            drawCirlce(redCircle);
            drawOctagon(greenOctagon);
            drawRectangle(blueRectangle);
            drawRectangle(blackRectangle);
            drawStar(greenStar);
        }
    }


});