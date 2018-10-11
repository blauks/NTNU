/* Part 2 */
console.log('PART 2');
/*I use a for loop to go through all the numbers from 1 to 20.*/ 
for(let x = 1; x < 21; x++){
    console.log(x);
}

/* Part 3 */
console.log('PART 3');

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

/*Goes through all the elements in the numbers list and checks if there is anything after the comma when you
modulo the number with 3 or 5, if there is it replaces the number with either eple or kake, if there is not
it prints out the number*/
for(let y = 0; y<numbers.length;y++){
    if(numbers[y] % 3 === 0 && numbers[y] % 5 !== 0){
        console.log("eple");
    }
    else if(numbers[y] % 5 === 0 && numbers[y] % 3 !== 0){
        console.log("kake");
    }
    else if(numbers[y] % 3 === 0 && numbers[y] % 5 === 0){
        console.log("eplekake");
    }
    else{
        console.log(numbers[y]);
    }
}

/* Part 4 */
/*Uses document.GetElementById('title') to look for elements in the HTML code with ID title, and then replaces
its content with Hello, Javascript*/
document.getElementById('title').innerText = "Hello, JavaScript";
/* Part 5 */
function changeDisplay () {
    /*When the function changeDisplay is called, it will change the element with ID magic display to none*/
    document.getElementById('magic').style.display = "none";
}

function changeVisibility () {
    /*When the function is called the element with id magic will change its display to block and 
    visibility to hidden*/
    document.getElementById('magic').style.display = "block";
    document.getElementById('magic').style.visibility = "hidden";
}

function reset () {
    /*When the reset function is called the element with id magic will change its display to block and 
    visibility to visible*/
    document.getElementById('magic').style.display = "block";
    document.getElementById('magic').style.visibility = "visible";
}

/* Part 6 */
const technologies = [
    'HTML5',
    'CSS3',
    'JavaScript',
    'Python',
    'Java',
    'AJAX',
    'JSON',
    'React',
    'Angular',
    'Bootstrap',
    'Node.js'
];

/* The for loop goes through all the elements in the list, and then adds it in the unordered list with id tech
 as list elements */
for(let T = 0; T < technologies.length;T++){
    document.getElementById("tech").innerHTML += "<li>" + technologies[T] + "</li>"
}