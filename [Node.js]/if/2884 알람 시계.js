const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.setAlarm = function(time){
    if (time[1]>=45) return console.log(time[0],time[1]-45)
    else if (time[1]<45){
        if (time[0]!=0) return console.log(time[0]-1,15+time[1])
        else return console.log(23,15+time[1])
    }
}

rl.on("line",function(line){
    input = line.split(' ').map(e=>parseInt(e))
    this.setAlarm(input)
    rl.close()
}).on("close",()=>process.exit())
