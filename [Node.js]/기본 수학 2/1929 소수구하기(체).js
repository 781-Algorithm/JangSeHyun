const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.find_prime = function(m,n){
    let temp = new Array(n+1).fill(true)
    temp[0] = false
    temp[1] = false
    for(let i=2;i<=Math.sqrt(n)+1;i++){
        if (temp[i]){
            let j=2
            while(i*j<=n){
                temp[i*j]=false
                j+=1
            }
        }
    }
    temp.forEach((val,idx)=>{
        if((val)&&idx>=m){
            console.log(idx)
        }
    })
    return
}

rl.on('line',function(line){
    input = line.split(' ').map(el=>Number(el))
    rl.close()
}).on('close',function(){
    this.find_prime(input[0],input[1])
    process.exit()
})