const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = line.split(" ").map(el=>Number(el))
    this.close()
}).on('close',function(){
    input[2]<=input[1] ? console.log(-1) : console.log(Math.floor(1+input[0]/(input[2]-input[1])))
    process.exit()
})