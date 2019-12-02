const fs = require('fs');

const program = async () => {
  const text = (await fs.readFileSync('./input.txt')).toString();
  const totalFuel = text
    .split('\n')
    .filter(str => str.length > 1)
    .map(mass => +mass)
    .map(mass => Math.floor(mass / 3) - 2)
    .reduce((curr, add) => curr + add);
  console.log(totalFuel);
}

program();
