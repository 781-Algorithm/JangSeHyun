const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
rl.solution = function(num){
    let count = 0
    for(let i=1;i<=num;i++){
        if(i<100){
            count+=1
            continue
        }
        let arr = Array.from(String(i)).map(e=>parseInt(e))
        count = (arr[0]+arr[2]==2*arr[1]) ? count+1 : count
    }
    return count
}
let input;
rl.on('line',function(line){    
    input = parseInt(line)
    rl.close();
}).on('close',function(){
    console.log(this.solution(input))
    process.exit()
})