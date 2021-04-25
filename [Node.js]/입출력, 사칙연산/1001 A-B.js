readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line',function(line){
    input = line.split(' ').map(str=>parseInt(str))
    console.log(input[0]-input[1]);
    rl.close();
}).on('close',()=>process.exit());