async function loadChart(){

let res = await fetch("http://127.0.0.1:5000/transactions")
let data = await res.json()

let categories={}
data.forEach(t=>{
if(t.type==="expense"){
categories[t.category]=(categories[t.category]||0)+t.amount
}
})

let labels=Object.keys(categories)
let values=Object.values(categories)

new Chart(document.getElementById("spendingChart"),{
type:"pie",
data:{
labels:labels,
datasets:[{
data:values
}]
}
})
}

loadChart()