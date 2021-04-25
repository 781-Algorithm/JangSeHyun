const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = []
let count = 0

rl.on('line', function(line){
    input.push(line)
    count++
    count==2 ? rl.close() : undefined
}).on('close',function(){

    const A = input[0]
    const B = input[1]

    console.log(A*(B%10))
    console.log(A*(parseInt((B%100)/10)))
    console.log(A*parseInt(B/100))
    console.log(A*B)

    process.exit()
});