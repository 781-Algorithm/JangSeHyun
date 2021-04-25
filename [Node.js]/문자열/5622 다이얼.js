const readline = require('readline')
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const dial ={A:3,B:3,C:3,D:4,E:4,F:4,G:5,H:5,I:5,J:6,K:6,L:6,M:7,N:7,O:7,P:8,Q:8,R:8,S:8,T:9,U:9,V:9,W:10,X:10,Y:10,Z:10}

rl.on('line',function(line){    
    input = line.split("")
    console.log(input.reduce((pre,cur)=>pre+dial[cur]))
    rl.close()
}).on('close',()=>process.exit())