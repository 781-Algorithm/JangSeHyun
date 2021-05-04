const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = Number(line)
    this.close()
}).on('close',function(){
    let div = parseInt(input/5)
    if (input%5==0){
        console.log(div)
        process.exit()
    }
    while(div>=0){
        let remain = input - div*5
        if (remain%3===0){
            console.log(parseInt(remain/3)+div)
            process.exit()
        }
        div-=1
    }
    console.log(-1)
    process.exit()
})