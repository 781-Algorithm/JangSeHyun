const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    input = line.split(" ").map(e=>parseInt(e))
    if(input[0]+input[1]===0){
        rl.close();
    }
    else {console.log(input[0]+input[1])}
}).on('close', function () {
    process.exit();
});