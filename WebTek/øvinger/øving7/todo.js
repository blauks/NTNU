const textField = document.getElementById("textInput")
const addButton = document.getElementById("buttonAdd")
const todoList = document.getElementById("list")

var tasks = []

function addTask(){
    let todo = textField.value   
    if(todo != ""){
        todoList.innerHTML += "<li><input type='checkbox'>"+todo+"</input></li>"
    }
}

