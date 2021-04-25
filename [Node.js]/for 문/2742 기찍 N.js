const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line",function(line){
    input = parseInt(line)
    rl.close()
}).on("close",()=>{
    let result = ''
    for(let i=input;i>0;i--){
        result+=i+'\n'
    }
    console.log(result)
    process.exit()
})