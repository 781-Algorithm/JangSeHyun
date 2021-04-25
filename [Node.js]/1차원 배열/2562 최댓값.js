const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

let input = []

rl.on('line',function(line){    
    input.push(parseInt(line))
}).on('close',function(){
    let max_idx = -1
    let max = -1
    for(let i in input){
        if(input[i]>max){
            max = input[i]
            max_idx = i
        }
    }
    console.log(max)
    console.log(Number(max_idx)+1)
    process.exit()
})