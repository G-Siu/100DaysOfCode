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

const cash = document.getElementById("cash");
const purchaseBtn = document.getElementById("purchase-btn");
const changeInDrawer = document.getElementById("change-in-drawer");

const calculateChange = (cash) => {
    changeOwed = (Number(cash.value) - price).toFixed(2);
    console.log(changeOwed) 
}

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

