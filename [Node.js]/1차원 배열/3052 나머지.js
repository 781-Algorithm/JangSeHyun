const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let input = []
rl.on('line',function(line){    
    input.push(line)
}).on('close',function(){
    let mods = input.map(el=>el%42)
    let dict = {}
    mods.forEach(function(e){
        if(dict[`${e}`]===undefined){
            dict[`${e}`]=1
        }
        else{dict[`${e}`]+=1}
    })
    console.log(Object.keys(dict).length)
    process.exit()
})