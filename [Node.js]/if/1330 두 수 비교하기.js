const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line",function(line){
    input = line.split(' ').map(e=>parseInt(e))
    const A = input[0]
    const B = input[1]
    if (A>B) console.log('>')
    else if (A<B) console.log('<')
    else console.log('==')
    rl.close()
    
}).on("close",()=>process.exit())