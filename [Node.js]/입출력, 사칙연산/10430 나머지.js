const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', function(line){
    input = line.split(' ').map(str=>parseInt(str));
    
    const A = input[0]
    const B = input[1]
    const C = input[2]

    console.log((A+B)%C)
    console.log(((A%C) + (B%C))%C)
    console.log((A*B)%C)
    console.log(((A%C) * (B%C))%C)

    rl.close()
}).on('close',()=>process.exit());