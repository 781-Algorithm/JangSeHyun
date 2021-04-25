const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

rl.on('line',function(line){    
    input = Number(line)
    this.close();
}).on('close',function(){
    let pl = 1;
    while(true){
        let upper = pl*(pl+1)/2
        if(input<=upper){
            let idx = upper-input
            if(pl%2===0){console.log(`${pl-idx}/${idx+1}`)}
            else{console.log(`${idx+1}/${pl-idx}`)}
        break
        }
        pl+=1
    }
    process.exit()
})