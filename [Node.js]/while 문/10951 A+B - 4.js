const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let output = "";
rl.on('line', function (line) {
    const numbers = line.split(" ");
    output += +numbers[0]+ +numbers[1] +"\n"
}).on('close', function () {
    console.log(output);
      
    process.exit();
});