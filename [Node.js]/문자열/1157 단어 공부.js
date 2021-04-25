const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
rl.checkStr = function(str){
    let count = new Array(26)
    count.fill(0)
    Array.from(str).forEach(str=>count[str.charCodeAt(0)-65]+=1)
    let max = count.reduce((pre,cur)=>pre>cur?pre:cur)
    return count.indexOf(max)===count.lastIndexOf(max)? String.fromCharCode(count.indexOf(max)+65) : '?'
}

rl.on('line',function(line){    
    input = line.toUpperCase()
    rl.close()
}).on('close',function(){
    console.log(this.checkStr(input))
    process.exit()
})