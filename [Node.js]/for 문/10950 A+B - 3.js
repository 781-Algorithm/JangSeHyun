const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const array = []
const onInput = (input) => array.push(input)
const onClose = ()=>{
    for (let i=1;i<=array[0];i++){
        const [num1,num2] = array[i].split(' ')
        console.log(Number(num1)+Number(num2))
    }
    process.exit();
}

rl.on('line',onInput).on('close',onClose);

// 뭔가 이거 좀 깔끔하긴 해, 근데 얘 종료를 자동으로 못시키네..