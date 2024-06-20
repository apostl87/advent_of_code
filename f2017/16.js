function firstStar(input){
    let prog = "abcdefghijklmnop".split('');
    input.split(',').forEach((move) => {
        parseMove(move, prog);
    });
    console.log("First Star: ", prog.join(''));
}

function secondStar(input){
    let prog = "abcdefghijklmnop".split('');
    let inputs = input.split(',');
    let startPoint = prog.join('');

    let iterations = 1000000000;
    for (let i = 0; i < iterations; i++){
        inputs.forEach((move) => parseMove(move, prog));
        if (prog.join('') === startPoint) {
            console.log(i)
            console.log(prog)
            i += (Math.floor(iterations/(i+1))-1) * (i+1);
        }
    }
    console.log("Second Star: ", prog.join(''));
}

function parseMove(move, prog){
    if (move[0] === 's'){ //spin
        let num = parseInt(move.substr(1));
        prog.unshift(...prog.splice(-num, num));
    } else if (move[0] === 'x') { //position swap
        let pos = move.substr(1).split('/');
        [prog[pos[0]], prog[pos[1]]] = [prog[pos[1]], prog[pos[0]]];
    } else { // program swap
        let pos = move.substr(1).split('/');
        let idx1 = prog.indexOf(pos[0]);
        let idx2 = prog.indexOf(pos[1]);
        [prog[idx1], prog[idx2]] = [pos[1], pos[0]];
    }
}

const fs = require('node:fs');
let data
try {
  data = fs.readFileSync('16.in', 'utf8');
} catch (err) {
}

firstStar(data)
secondStar(data)