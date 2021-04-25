const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let array= []

rl.on('line', function (line) {
    input = line.split(" ").map(e=>parseInt(e))
    array.push(input)
}).on('close', function () {
    let [n,x] = array[0]
    let numbers = array[1]
    console.log(...numbers.filter(el => el<x))
    process.exit();
});