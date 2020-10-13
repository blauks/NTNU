var s = document.getElementById("s-circ");
var m = document.getElementById("m-circ");
var l = document.getElementById("l-circ");

$(document).ready(function(){
    $("#s-circ").mousedown(function(event){
        movePol(event, s)
        $("#s-circ").mouseup(function(){
            $("#s-circ").off("mousemove");
        });
      }
    );
  });

$(document).ready(function(){
    $("#m-circ").mousedown(function(event){
        movePol(event, m)
        $("#m-circ").mouseup(function(){
            $("#m-circ").off("mousemove");
        });
      }
    );
  });

$(document).ready(function(){
    $("#l-circ").mousedown(function(event){
        movePol(event, l)
        $("#l-circ").mouseup(function(){
            $("#l-circ").off("mousemove");
        });
      }
    );
  });

movePol = function(event, target){
    let shiftX = event.clientX - target.getBoundingClientRect().left-10;
    let shiftY = event.clientY - target.getBoundingClientRect().top-10;

    function moveAt(pageX, pageY) {
      target.setAttribute("cx", pageX - shiftX);
      target.setAttribute("cy", pageY - shiftY);
      console.log(target);
    }
    $(document).ready(function(){
      if(target=s){
          $("#s-circ").mousemove(function(event){
        
              moveAt(event.pageX, event.pageY);
            }
          );

      } else if(target=m){
          $("#m-circ").mousemove(function(event){
        
            moveAt(event.pageX, event.pageY);
            }
          );

      } else if(target=l){
          $("#l-circ").mousemove(function(event){
        
            moveAt(event.pageX, event.pageY);
           }
            );

      } 
    });
      
    }

    
