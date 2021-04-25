const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = line.split(" ").map(el=>Number(el))
    this.close()
}).on('close',function(){
    if(input[0]===input[2]){
        console.log(1)
    }
    else{
        console.log(Math.ceil((input[2]-input[0])/(input[0]-input[1]))+1)
    }
    process.exit()
})