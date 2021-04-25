const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const croatian = ['c=','c-','dz=','d-','lj','nj','s=','z=']
let result = 0

rl.on('line',function(line){    
    input = line
    for(i=0;i<croatian.length;i++){
        let re = new RegExp(croatian[i])
        while(true){
            if(re.exec(input)){
                result+=1
                input = input.replace(croatian[i],' ')
            }
            else break
        }
    }
    
    result += input.replace(/ /g,"").length
    console.log(result)
    rl.close()
}).on('close',()=>process.exit())