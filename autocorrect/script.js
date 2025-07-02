
let names = ["fart","poop","shit"];

let displayse = document.getElementById("displayse");

let testinput = document.getElementById("input");

testinput.value="";

testinput.addEventListener('input',()=>{
    //if (testinput.value[0] == names[0]){displayse.textContent ==names[0]}
 for (item in names){
    if (item ===  testinput.value){console.log(item)}
 }
        
})