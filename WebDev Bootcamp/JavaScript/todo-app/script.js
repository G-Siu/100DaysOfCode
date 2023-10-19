const taskInput = document.getElementById("new");
const addButton = document.getElementById("add");
const tasks = document.getElementById("tasks");

addButton.addEventListener("click", addNewItem);
taskInput.addEventListener("keyup", processKeyPress);

const items = getItems();

for (let item of items) {
    const li = createElementForTask(item);
    tasks.appendChild(li);
}

function addNewItem() {
    const task = {
        value: taskInput.value,
        complete: false
    }

    items.push(task);

    let newItem = createElementForTask(task);
    tasks.appendChild(newItem);

    taskInput.value = "";
    taskInput.focus();
    addButton.disabled = true;
}

function createElementForTask(item) {
    const template = document.getElementById("taskTemplate");
    const newListItem = template.content.cloneNode(true);

    const text = newListItem.querySelector(".item-text");
    const checkbox = newListItem.querySelector(".item-check");
    const deleteButton = newListItem.querySelector(".delete");

    text.innerText = item.value;
    checkbox.checked = item.complete;

    checkbox.onchange = function (event) {
        item.complete  = event.target.checked;
        saveItems();
    };

    deleteButton.onclick = function (event) {
        event.target.closest("li").remove();
        items.splice(items.indexOf(item), 1);
        saveItems();
    };

    return newListItem;
}

function processKeyPress(event) {
    addButton.disabled = event.target.value.trim() === "";

    if (event.key === "Enter" && !addButton.disabled) {
        addNewItem();
    }
}

function getItems() {
    const noItemsFound = "[]";
    const itemsJSON = localStorage.getItem("items") || noItemsFound;
    return JSON.parse(itemsJSON);
}

function saveItems() {
    const data = JSON.stringify(items);
    localStorage.setItem("items", data);
}