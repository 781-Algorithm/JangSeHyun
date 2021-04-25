const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let input = []

rl.avgPer = function(array){
    [num,...data] = array
    let avg = (data.reduce((pre,cur)=>pre+cur))/num
    let percent = data.filter(e=>e>avg).length/num
    console.log(`${(percent*100).toFixed(3)}%`)
    return
}

rl.on('line',function(line){
    input.push(line.split(" ").map(e=>parseInt(e)))
}).on('close',function(){
    for(let i=1;i<=input[0][0];i++){
        rl.avgPer(input[i])
    }
    process.exit()
})