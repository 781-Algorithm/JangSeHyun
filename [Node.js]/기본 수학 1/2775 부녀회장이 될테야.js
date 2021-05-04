const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
let array = []
let dp = Array.from(Array(15),()=>Array(15).fill(0)) // 15x15 배열 초기화

dp[0] = dp[0].map((el,idx)=>dp[0][idx]=idx)

for(let i=1;i<=14;i++){
    for(let j=1;j<=14;j++){
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
    }
}

rl.on('line',function(line){
    array.push(Number(line))
}).on('close',function(){
    let limit = 1
    for(let i=1;limit<=array[0];i+=2){
        console.log(dp[array[i]][array[i+1]])
        ++limit
    }
})