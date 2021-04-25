const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', function(line){
    input = line.split(' ').map(str=>parseInt(str));
    const A = input[0]
    const B = input[1]
    console.log(A+B)
    console.log(A-B)
    console.log(A*B)
    console.log(parseInt(A/B))
    console.log(A%B)
    rl.close()
}).on('close',()=>process.exit());