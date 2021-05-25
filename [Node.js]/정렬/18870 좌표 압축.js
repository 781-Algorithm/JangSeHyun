const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let array = []
let dict = {}
let result = ''

rl.on('line',function(line){    
    array.push(line.split(" ").map(el=>Number(el)))
}).on('close',function(){
    const sorted_set = new Set([...array[1]].sort((a,b)=>a-b))
    Array.from(sorted_set).forEach((val,idx)=>dict[val]=idx)
    for(let i=0;i<array[0][0];i++){
        result += dict[array[1][i]]+' '
    }
    console.log(result)
    process.exit()
})