const fs = require('fs');

const massToFuel = (mass) => {
  const fuel = Math.floor(mass / 3) - 2;
  if (fuel <= 0) {
    return 0;
  }
  return fuel + massToFuel(fuel);
}

const program = async () => {
  const text = (await fs.readFileSync('./input.txt')).toString();
  const totalFuel = text
    .split('\n')
    .filter(str => str.length > 1)
    .map(mass => +mass)
    .map(massToFuel)
    .reduce((curr, add) => curr + add);
  console.log(totalFuel);
}

program();
