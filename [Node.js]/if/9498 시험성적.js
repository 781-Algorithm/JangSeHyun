const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.examScore = function(score){
    if (score >= 90) return "A";
    else if (score >= 80) return "B";
    else if (score >= 70) return "C";
    else if (score >= 60) return "D";
    else return "F";
}
    
rl.on("line",function(line){
    input = parseInt(line)
    console.log(this.examScore(line))
    rl.close()
}).on("close",()=>process.exit())
