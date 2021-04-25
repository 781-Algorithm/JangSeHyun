const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let input = []

rl.on('line',function(line){
    input.push(line.split(" ").map(e=>parseInt(e)))
}).on('close',function(){
    let max = input[1].reduce((pre,cur)=>pre>cur ? pre : cur)
    let temp = input[1].map(e=>(e/max)*100)
    const result = (temp.reduce((pre,cur)=>{return pre+cur}))/input[0][0]
    console.log(result)
    process.exit()
})