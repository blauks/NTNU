const textField = document.getElementById("textInput")
const addButton = document.getElementById("buttonAdd")
const todoList = document.getElementById("list")

var tasks = []

function addTask(){
    let todo = textField.value
    if(todo != "" && !tasks.includes(todo)){
        console.log(!tasks.includes(todo))
        todoList.innerHTML = "<li><input onClick='checkboxFunc(this.name)' name="+todo+" type='checkbox'><label id="+todo+">"+todo+"</label></input></li>" + todoList.innerHTML
        tasks.push(todo)
        console.log(tasks)
    }
}

function checkboxFunc(eId){ //eId = element ID
    if(document.getElementById(eId).style.textDecoration != "line-through"){
        document.getElementById(eId).style.textDecoration = "line-through"
    }
    else{
        document.getElementById(eId).style.textDecoration = "none"   
    }
} //Did not manage to create a variable for document.getElementById(eId).style.textDecoration