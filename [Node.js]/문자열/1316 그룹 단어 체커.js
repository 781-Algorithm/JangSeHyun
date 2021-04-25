const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

function groupWordChecker(str){
    let wordIdx = {}
    for(let i=0;i<str.length;i++){
        if(wordIdx[str[i]]!==undefined){
            if(i-wordIdx[str[i]]>1){
                return false
            }
        }
        wordIdx[str[i]] = i
    }
    return true
}

let words = []

rl.on('line',function(line){    
    words.push(line)
}).on('close',function(){
    let result = 0
    for(let i=1;i<words.length;i++){
        if(groupWordChecker(words[i])) {result+=1}
    }
    console.log(result)
    process.exit()
})