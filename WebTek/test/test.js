function farge(){
    var r = 0;
        var rb = true;
        var rm = false;
    var g = 0;
        var gb = false;
        var gm = false;
    var b = 0;
        var bb = false;
        var bm = false;
    var etappe = 0;
    var a = 1;
    setInterval(() => {
        if(etappe == 0 && r<=255){
            r++;
        }
        else if(b>0 && etappe == 0 && r>255){
            b--;
        }
        else if(etappe == 0 && r>255 && b == 0){
            etappe = 1;
        }

        if(etappe == 1 && g<=255){
            g++;
        }
        else if(g>255 && etappe == 1 && r>0){
            r--;
        }
        else if(r == 0 && etappe == 1){
            etappe = 2;
        }

        if(etappe == 2 && b<=255){
            b++;
        }
        else if(etappe == 2 && b>255 && g>0){
            g--;
        }
        else if(g == 0 && etappe == 2){
            etappe = 0;
        }

        console.log(r+","+g+","+b)

        document.body.style.backgroundColor = "rgb("+r+","+g+","+b+","+a+")";
    }, 25);
}