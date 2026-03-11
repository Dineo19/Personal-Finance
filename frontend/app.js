async function loadHealth(){

let res = await fetch("http://127.0.0.1:5000/health")
let data = await res.json()

document.getElementById("health").innerText =
"Financial Health Score: "+data.score
}

async function loadWarnings(){

let res = await fetch("http://127.0.0.1:5000/warnings")
let data = await res.json()

document.getElementById("warnings").innerText =
data.join("\n")
}

async function loadSubscriptions(){

let res = await fetch("http://127.0.0.1:5000/subscriptions")
let data = await res.json()

document.getElementById("subscriptions").innerText =
data.join("\n")
}

async function addTransaction(){

let type=document.getElementById("type").value
let amount=document.getElementById("amount").value
let category=document.getElementById("category").value
let description=document.getElementById("description").value

await fetch("http://127.0.0.1:5000/add_transaction",{
method:"POST",
headers:{'Content-Type':'application/json'},
body:JSON.stringify({
type:type,
amount:amount,
category:category,
description:description,
date:new Date().toISOString().split("T")[0]
})
})

alert("Transaction Added")
}

loadHealth()
loadWarnings()
loadSubscriptions()