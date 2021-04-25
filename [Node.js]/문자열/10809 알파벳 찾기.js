const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
rl.checkStr = function(str){
    let result = new Array(26)
    for(let i=0;i<26;i++){result[i]=-1}
    strArr = Array.from(str)
    for(let idx in strArr){
        ascii = strArr[idx].charCodeAt(0)-97
        result[ascii] = result[ascii]===-1 ? idx : result[ascii]  
    }
    console.log(...result)
}

rl.on('line',function(line){    
    input = line
    rl.close()
}).on('close',function(){
    this.checkStr(input)
    process.exit()
})