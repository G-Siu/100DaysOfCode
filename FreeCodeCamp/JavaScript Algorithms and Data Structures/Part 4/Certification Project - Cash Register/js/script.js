let price = 1.87;
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


const cash = document.getElementById("cash");
const purchaseBtn = document.getElementById("purchase-btn");
const changeInDrawer = document.getElementById("change-in-drawer");
const display = document.getElementById("display");

const calculateChange = (cash) => {
    let changeOwed = (Number(cash.value) - price).toFixed(2);
    // console.log(changeOwed)
    const changeGiven = []
    for (let i = actualChange.length; i > -1; i--) {
        const changePerUnit = Math.floor(changeOwed / cashValue[i])
        const changeToGive = changePerUnit * cashValue[i];
        // console.log(changePerUnit)
        // console.log(cashValue[i])
        // console.log(changeToGive)
        // changeOwed -= changeToGive;
        if (changeToGive > 0) {
            const status = `${cid[i][0]}: $${changeToGive}`;
            changeGiven.push(status)
        }
        // console.log(changeOwed)
        // console.log(changeGiven)
        // console.log(actualChange[i])
    }
}

display.innerHTML = `<p>Total: $${price}</p>`
// Format change names and insert HTML, get change amount into array
const actualChange = [];
for (const change of cid) {
    if (change[0].includes(" ")) {
        change[0] = change[0].split(" ")[1];
    }
    changeSplit = change[0].split("");
    if (changeSplit.at(-1) === "Y") {
        changeSplit.pop();
        changeSplit.push("IES");
    } else {
        changeSplit.push("S");
    }
    changeSplitLower = changeSplit[0] + changeSplit.slice(1).join("").toLowerCase();
    changeInDrawer.innerHTML += `<p>${changeSplitLower}: $${change[1]}</p>`
    actualChange.push(change[1]);
}

purchaseBtn.addEventListener("click", () => {
    /* 4.When the value in the #cash element is less than price, an alert should appear with the text Customer does not have enough money to purchase the item
    5.When the value in the #cash element is equal to price, the value in the #change-due element should be No change due - customer paid with exact cash */
    if (!cash.value || cash.value < price) {
        alert("Customer does not have enough money to purchase the item");
        return;
    } else if (Number(cash.value) === price) {
        alert("No change due - customer paid with exact cash");
        return;
    }
    calculateChange(cash);
    
});

