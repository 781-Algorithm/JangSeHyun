const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let result = 0

rl.on('line',function(line){
    input = parseInt(line)
    rl.close()
}).on('close',()=>{
    for(let i=1;i<=input;i++){
        result+=i
    }
    console.log(result)
    process.exit()
})