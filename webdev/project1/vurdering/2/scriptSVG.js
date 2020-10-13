var drags, dragm, dragl, dragd

$(document).ready( function(){
    $("#s-circ").mousedown(function (event) { 
        drags = true;
    });
    $("#m-circ").mousedown(function (event) { 
        dragm = true;
    });
    $("#l-circ").mousedown(function (event) { 
        dragl = true;
    });
    
    $(document).mouseup(function (event){
        drags=false;
        dragm=false;
        dragl=false;
    })

    
    $("#s-circ").mousemove(function(event){
        if(drags){
            var x = event.clientX - $("svg").offset().left;
            var y = event.clientY - $("svg").offset().top;
            console.log("small: ",x, y)
            $(this).css("cx", x);
            $(this).css("cy", y);
        }
    })
    $("#m-circ").mousemove(function(event){
        if(dragm){
            var x = event.clientX - $("svg").offset().left;
            var y = event.clientY - $("svg").offset().top;
            console.log("Medium: ", x, y)
            $(this).css("cx", x);
            $(this).css("cy", y);
        }
    })
    $("#l-circ").mousemove(function(event){
        if(dragl){
            var x = event.clientX - $("svg").offset().left;
            var y = event.clientY - $("svg").offset().top;
            console.log("Large: ",x, y)
            $(this).css("cx", x);
            $(this).css("cy", y);
        }
    })
    $("#diamond-pol").mouseenter(function(event){
            $(this).css('fill', 'black');
               
    }).mouseleave(function(event){
        $(this).css('fill', 'yellow')
          
    })
    $("#left-pol").mouseenter(function(event){
        $(this).css('fill', 'orange');
           
    }).mouseleave(function(event){
    $(this).css('fill', 'green')
      
    })
    $("#right-pol").mouseenter(function(event){
        $(this).css('fill', 'purple');
           
    }).mouseleave(function(event){
    $(this).css('fill', 'grey')
      
    })
    






});
