console.log("Hei")

const a = "hei";

console.log(a)

let b = "ok";

b = 2

console.log(b)

function problem(t){
    sum = 0;
    for(let i = 0; i<t;i++){
        if(i % 3 === 0 || i % 5 === 0){
            sum += i;
        }
    }
    return sum;
}

console.log(problem(1000));