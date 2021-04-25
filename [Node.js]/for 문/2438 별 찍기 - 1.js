const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let output = "";

rl.on('line', function (line) {
    input = Number(line)
    for(let i=1;i<=input;i++){
        output+="*".repeat(i)+"\n"
    }
    rl.close()
}).on('close', function () {
    console.log(output)
    process.exit();
});