const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = Number(line)
    this.close();
}).on('close',function(){
    if(input===1){console.log(1)}
    else{
        let result = 1
        while(true){
            let lower = 3*result*(result-1)+2;
            let upper = 3*(result+1)*(result)+1;
            if ((input>=lower)&&(input<=upper)){break}
            result+=1
        }
        console.log(1+result)
    }
    process.exit()
})