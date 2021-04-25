const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.getCycle = function(number){
    let cycle = 0;
    while(true){
        number = (number%10)*10+parseInt((parseInt(number/10)+number%10)%10)
        ++cycle
        if (number === input){
            break
        }
    }
    return cycle
}

rl.on('line', function (line) {
    input = parseInt(line)
    console.log(this.getCycle(input))
    rl.close()
}).on('close', ()=>process.exit());