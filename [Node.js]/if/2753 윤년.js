const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.leapYear = function(year){
    return ((year%4==0)&&(year%100!=0)||(year%400==0)) ? 1 : 0
}
    
rl.on("line",function(line){
    input = parseInt(line)
    console.log(this.leapYear(line))
    rl.close()
}).on("close",()=>process.exit())
