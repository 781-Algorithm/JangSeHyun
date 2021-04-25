function notSelfNum(){
    for(let i=1;i<=9990;i++){
        let idx = i+Array.from(String(i)).map(e=>parseInt(e)).reduce((pre,cur)=>pre+cur)
        result[idx]=false
    }
}

let result = []
let answer = ''
for(let i=0;i<=10000;i++){result[i]=true}
notSelfNum()
for(let i=1;i<=10000;i++){answer = result[i] ? answer+String(i)+'\n' : answer }
console.log(answer);