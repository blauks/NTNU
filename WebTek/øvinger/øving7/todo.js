const textField = document.getElementById("textInput")
const addButton = document.getElementById("buttonAdd")
const todoList = document.getElementById("list")



var tasks = [] //I use this list to check if the task already has been added and only store the todo names
var tasksAndDate = [] //To store the task and the variable from the now function

//I decided to add another list variabel because it only having the names makes it easier to use in my code,
//and the tasksAndDate could be useful if I ever want to check when it was made

function addTask(){
    if(todo.trim() != "" && !tasks.includes(todo)){
       /* todoList.innerHTML = "<li><input onClick='checkboxFunc(this.name)' name="+todo+" type='checkbox'><label id="+todo+">"+todo+"</label></input></li>" + todoList.innerHTML
        //I could have used appendchild and all that to add tasks, but this method was easier for me
        tasks.push(todo)
        tasksAndDate.push(todo,Date.now())
        textField.value = "" */

        

    }
    updateCompletedlist()
    console.log(tasks,":",tasksAndDate)
}

function checkboxFunc(lId){ //lId = the label inside the list elements ID
    if(document.getElementById(lId).style.textDecoration != "line-through"){
        document.getElementById(lId).style.textDecoration = "line-through"
    }   
    else{
        document.getElementById(lId).style.textDecoration = "none"   
    }
    updateCompletedlist()
} //Did not manage to create a variable for document.getElementById(eId).style.textDecoration

function updateCompletedlist(){
    let howMany = 0
    for(x in tasks){
       if(document.getElementById(tasks[x]).style.textDecoration == "line-through"){
            howMany = howMany + 1
       }
    }
    document.getElementById("completed").innerHTML = howMany+"/"+tasks.length+" completed"
}

//small bug with my program is that when you add a new task to your list and one of the checkboxes in the list
//are already checked the checkbox will uncheck but the task will keep its line through