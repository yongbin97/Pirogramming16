function init(){
    document.getElementById("add_btn").addEventListener("click", appendList, false); 
    document.getElementById("select_del").addEventListener("click", del_select, false);
    document.getElementById("last_del").addEventListener("click", del_last, false);
    document.getElementById("all_del").addEventListener("click", del_all, false);
}

function appendList(){
    const inputValue = document.getElementById("appendList").value;
    const todo = document.getElementById("todo_ul");
    
    const new_li = document.createElement("li");
    todo.appendChild(new_li);
    
    const div = document.createElement("div");
    div.setAttribute("class", "check-box");
    new_li.appendChild(div);

    const checkbox = document.createElement("input");
    checkbox.setAttribute("type", "checkbox");
    div.appendChild(checkbox);

    const div2 = document.createElement("div");
    div2.setAttribute("class", "todo-content");
    div2.innerText = inputValue;
    new_li.appendChild(div2);

    document.getElementById("appendList").value = ""
    document.getElementById("appendList").focus()
}

function del_select(){
    const list = document.getElementById("todo_ul")
    const boxes = list.querySelectorAll("input")

    for (const box of boxes){
        if(box.checked){
            box.parentNode.parentNode.remove()
        }
    }
}

function del_last(){
    const list = document.getElementById("todo_ul")
    const last_li = list.lastChild;
    last_li.remove()
}

function del_all(){
    const list = document.getElementById("todo_ul")
    const boxes = list.querySelectorAll("input")

    for (const box of boxes){
        box.parentNode.parentNode.remove()
        
    }
}


window.addEventListener("load", init, false);
