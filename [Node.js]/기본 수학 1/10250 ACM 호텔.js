const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let array = []

rl.findroom = function(h,w,n){
    let div = parseInt((n-1)/h) // 호수
    let mod = (n-1)%h // 층
    if (div<9) console.log(`${mod+1}0${div+1}`)
    else console.log(`${mod+1}${div+1}`)
    return
}

rl.on('line',function(line){
    array.push(line.split(" ").map(el=>Number(el)))
}).on('close',function(){
    for(let i=1;i<=array[0][0];i++){
        this.findroom(...array[i])    
    }
})