const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = line.trimLeft().trimRight().split(" ")
    rl.close()
}).on('close',function(){
    input[0]!=="" ? console.log(input.length) : console.log(0)
    process.exit()
})