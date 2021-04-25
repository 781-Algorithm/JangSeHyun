const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = line.split(" ")
    let a = parseInt(Array.from(input[0]).reverse().reduce((pre,cur)=>pre+String(cur)))
    let b = parseInt(Array.from(input[1]).reverse().reduce((pre,cur)=>pre+String(cur)))
    a > b ? console.log(a) : console.log(b)
    rl.close()
}).on('close',()=>process.exit())