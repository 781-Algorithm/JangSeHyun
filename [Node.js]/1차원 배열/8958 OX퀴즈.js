const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let input = []

rl.quizScore = function(array){
    let total = 0;
    let temp = 0;
    for(let val of array){
        if(val==='O'){++temp}
        else{temp=0}
        total += temp
    }
    return total
}

rl.on('line',function(line){
    input.push(line)
}).on('close',function(){
    for(let i=1;i<=input[0];i++){
        console.log(this.quizScore(input[i]))
    }
    process.exit()
})