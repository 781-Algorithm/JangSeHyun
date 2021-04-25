const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let points = []
let count = 0

rl.findQuad = function(points){
    if ((points[0]>0)&&(points[1]>0)) return 1;
    else if ((points[0]>0)&&(points[1]<0)) return 4;
    else if ((points[0]<0)&&(points[1]<0)) return 3;
    else return 2;
}

rl.on("line",function(line){
    points.push(parseInt(line))
    count++
    count==2 ? rl.close() : undefined
}).on("close",function(){
    console.log(this.findQuad(points))
    process.exit()
})
