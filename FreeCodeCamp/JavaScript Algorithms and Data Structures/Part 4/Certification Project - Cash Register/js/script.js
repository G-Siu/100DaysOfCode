let price = 3.26;
let cid = [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.1],
    ["QUARTER", 4.25],
    ["ONE", 90],
    ["FIVE", 55],
    ["TEN", 20],
    ["TWENTY", 60],
    ["ONE HUNDRED", 100],
];

const cashValue = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 100];
const changeDue = document.getElementById("change-due");
const cash = document.getElementById("cash");
const purchaseBtn = document.getElementById("purchase-btn");
const changeInDrawer = document.getElementById("change-in-drawer");
const display = document.getElementById("display");

const calculateChange = (cash) => {
    let changeOwed = Math.floor((Number(cash.value) - price) * 100) / 100;
    const changeGiven = [];
    const cidCopy = cid.map(a => {return [...a]});
    for (let i = cid.length - 1; i > -1; i--) {
        let changePerUnit = Math.floor(changeOwed / cashValue[i]); 
        if (changePerUnit > cidCopy[i][1] / cashValue[i]) {
            changePerUnit = cidCopy[i][1] / cashValue[i];
        }
        const changeToGive = changePerUnit * cashValue[i];
        if (changeToGive > 0) {
            const status = `${cidCopy[i][0]}: $${changeToGive}`;
            changeGiven.push(status);
            changeOwed -= Math.floor(changeToGive * 100) / 100;
            changeOwed = changeOwed.toFixed(2);
            cidCopy[i][1] -= changeToGive;
        }
        if (i === 0) {
            message(changeGiven, Math.floor(changeOwed * 100) / 100, cidCopy);
            changeInDrawer.innerHTML = "";
            calculateChangeInDrawer();
        }
    }
}

display.innerHTML = `<p>Total: $${price}</p>`;
// Format change names and insert HTML, get change amount into array
const calculateChangeInDrawer = () => {
    changeInDrawer.innerHTML = `<p><strong>Change in drawer:</strong></p>`
    for (const change of cid) {
        if (change[0].includes(" ")) {
            change[0] = change[0].split(" ")[1];
        }
        const changeSplit = change[0].split("");
        if (changeSplit.at(-1) === "Y") {
            changeSplit.pop();
            changeSplit.push("IES");
        } else {
            changeSplit.push("S");
        }
        const changeSplitLower = changeSplit[0] + changeSplit.slice(1).join("").toLowerCase();
        changeInDrawer.innerHTML += `<p>${changeSplitLower}: $${Math.floor(change[1] * 100) / 100}</p>`;
        }
}

const message = (arr, changeOwed, cidCopy) => {
    const isZero = (change) => change[1] === 0;
    console.log(cidCopy)
    if (changeOwed > 0) {
        changeDue.innerHTML = `<p>Status: INSUFFICIENT_FUNDS</p>`;
    } else if (arr && changeOwed === 0 && !cidCopy.every(isZero)) {
        cid = cidCopy.map(a => {return [...a]});
        changeDue.innerHTML = `<p>Status: OPEN</p>`
        for (let i = 0; i < arr.length; i++) {
            changeDue.innerHTML += `<p>${arr[i]}</p>`;
        }
    } else if (changeOwed === 0 && cidCopy.every(isZero)) {
        cid = cidCopy.map(a => {return [...a]});
        changeDue.innerHTML = `<p>Status: CLOSED</p>`
        for (let i = 0; i < arr.length; i++) {
            changeDue.innerHTML += `<p>${arr[i]}</p>`;
        }
    };
}

calculateChangeInDrawer();

purchaseBtn.addEventListener("click", () => {
    /* 4.When the value in the #cash element is less than price, an alert should appear with the text Customer does not have enough money to purchase the item
    5.When the value in the #cash element is equal to price, the value in the #change-due element should be No change due - customer paid with exact cash */
    if (!cash.value || cash.value < price) {
        alert("Customer does not have enough money to purchase the item");
        return;
    } else if (Number(cash.value) === price) {
        changeDue.innerHTML = "<p>No change due - customer paid with exact cash</p>";
        return;
    }
    calculateChange(cash);
    cash.value = "";
});