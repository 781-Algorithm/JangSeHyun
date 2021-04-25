const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

let input = []

rl.on('line',function(line){
    
    input[input.length] = line.split(" ").map(e=>parseInt(e))
    
}).on('close',function(){
    const array = input[1]
    console.log(array.reduce((pre,cur)=>pre<cur ? pre : cur),array.reduce((pre,cur)=>pre>cur ? pre : cur))
    // let max = 0
    // let min = 10000000
    // for(const el of input[1]){
    //     min = el<min ? el : min
    //     max = el>max ? el : max
    // }
    console.log(min,max)
    process.exit()
})