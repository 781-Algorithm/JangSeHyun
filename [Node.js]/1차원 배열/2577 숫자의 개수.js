const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

let input = []
let dict = []
for (let i=0;i<10;i++){dict[i]=0}

rl.on('line',function(line){    
    input.push(line)
}).on('close',function(){
    const result = Array.from(String(input[0]*input[1]*input[2]))
    result.forEach(value=>++dict[value])
    dict.forEach(value=>console.log(value))
    process.exit()
})