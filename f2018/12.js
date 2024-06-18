const fs = require('node:fs');

// Parse input
try {
    var input = fs.readFileSync('12.txt', 'utf8');
} catch (err) {
    console.error(err);
}
// Process input
let initial
let inputbody
[initial, inputbody] = input.split('\n\n');
initial = initial.split(" ").pop()
inputbody = inputbody.trim();

let evolution = Object.create(null);
inputbody.split('\n').forEach((item) => {
    let line = item.split(" ");
    evolution[line[0]] = line[2];
})

// Part 1
let state = initial
let offset = 0;
for (let i = 0; i < 20; i++) {
    state = state.replaceAll(".", " ")
    offset += state.search(/\S/) ? state.search(/\S/) : 0; // Change of the position the first index refers to due to trim in the next line
    state = "...." + state.trim().replaceAll(" ", ".") + "....";

    offset -= 2; // This is because we start building the new state
    // two indices lower than the first index of the current state

    let new_state = "";
    for (let i = 2; i < state.length - 3; i++) {
        let key = state[i - 2] + state[i - 1] + state[i] + state[i + 1] + state[i + 2];
        new_state += evolution[key];
    }
    state = new_state;
    console.log(offset, state)
}

// Print result
console.log(state)
let sum = Array.from(state).reduce((result, value, index) => {
    result += (value == "#") ? (offset + index) : 0;
    return result
}, 0)
console.log("Part 1", sum, offset)


// Part 2
let time = Date.now()
state = initial
offset = 0;
let known = []
let offsets = []
let cycle_length = null
let first_occurence = null
let next_occurence = null
let offset_delta = null
while (true) {
    state = state.replaceAll(".", " ")
    offset += state.search(/\S/) ? state.search(/\S/) : 0; // Change of the position the first index refers to due to trim in the next line
    state = state.trim();
    first_occurence = known.indexOf(state);
    if (first_occurence >= 0) {
        next_occurence = known.length
        cycle_length = next_occurence - first_occurence;
        offset_delta = offset - offsets[first_occurence];
        console.log("First occurence ", first_occurence, "\n", "Offset: ", offsets[first_occurence], known[first_occurence])
        console.log("This occurence ", next_occurence, "\n", "Offset: ", offset, state)
        console.log("Cycle length\n", cycle_length)
        break
    } else {
        known.push(state)
        offsets.push(offset)
    }

    offset -= 2; // This is because we start building the new state
    // two indices lower than the first index of the current state
    state = "...." + state.replaceAll(" ", ".") + "....";
    let new_state = "";
    for (let i = 2; i < state.length - 3; i++) {
        let key = state[i - 2] + state[i - 1] + state[i] + state[i + 1] + state[i + 2];
        new_state += evolution[key];
    }
    state = new_state;
}

// Calculate result for cycle-length 1
let N = 50_000_000_000
if (cycle_length == 1) {
    offset += offset_delta * (N - next_occurence);
}
let sum2 = Array.from(state).reduce((result, value, index) => {
    result += (value == "#") ? (offset + index) : 0;
    return result
}, 0)
console.log("Part 2", sum2, offset)
console.log("Execution time: ", Date.now() - time, " ms")


// Helper function
function getPrintable2DGrid(positions) {

    let xmin = Math.min(...positions.map(x => x[0]));
    let xmax = Math.max(...positions.map(x => x[0]));
    let ymin = Math.min(...positions.map(x => x[1]));
    let ymax = Math.max(...positions.map(x => x[1]));

    let dimX = xmax - xmin + 1;
    let dimY = ymax - ymin + 1;

    let stringGrid = '';
    if (dimX < 100 && dimY < 100) {
        let row = Array.apply(true, Array(xmax - xmin + 1)).map(() => '.')
        let grid = Array.apply(true, Array(ymax - ymin + 1)).map(() => [...row])

        positions.forEach((pos, i) => {
            grid[pos[1] - ymin][pos[0] - xmin] = '#';
        })
        stringGrid = grid.map(row => row.join('')).join('\n');
    } else {
        stringGrid = '';
    }
    return [stringGrid, dimX, dimY];
}
