const fs = require('node:fs');

// Parse input
try {
    var input = fs.readFileSync('10.txt', 'utf8');
} catch (err) {
    console.error(err);
}
input = input.split('\n');

// Init positions and velocities
let positions = Array()
let velocities = Array();
input.forEach(function (line) {
    const regex = /([-]*\d+)/g;
    let numbers = line.match(regex);
    numbers = numbers.reduce((arr, x) => arr.concat((+x)), [])

    positions.push([numbers[0], numbers[1]]);
    velocities.push([numbers[2], numbers[3]]);
})

// Helper function
function getPrintableGrid(positions) {

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

// Perform simulation
let k = 0
let result = ['', Infinity, Infinity]
let oldResult
while (true) {
    k += 1
    // Update positions
    velocities.forEach((vel, i) => {
        positions[i][0] += vel[0];
        positions[i][1] += vel[1];
    })

    // Get printable grid
    oldResult = [...result];
    result = getPrintableGrid(positions)

    // Break loop if dimensions get greater
    if (result[1] > oldResult[1] && result[2] > oldResult[2]) {
        console.log(oldResult[0])
        console.log(k - 1, ' seconds')
        break
    }

    // Safety exit
    if (k == 1000000) break;
}