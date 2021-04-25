const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let output = "";
let caseCount = 0;

rl.on('line', function (line) {
    const numbers = line.split(" ");
    if (numbers.length === 2) {
        caseCount++;
        output += `Case #${caseCount}: ${Number(numbers[0])} + ${Number(numbers[1])} = ${Number(numbers[0])+Number(numbers[1])}` +"\n";
    }
}).on('close', function () {
    console.log(output);
      
    process.exit();
});