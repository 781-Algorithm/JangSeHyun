const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let arr = [];
rl.on('line',function(line){    
    arr.push(line.split("").map(e=>parseInt(e)))
}).on('close',function(){
    console.log(arr[1].reduce((pre,val)=>pre+val))
    process.exit()
})