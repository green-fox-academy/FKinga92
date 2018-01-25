function getSumUntil(number) {
  let sum = 0;
  for (let i = 0; i <= number; i++) {
    sum += i;
  }
  return sum;
}

function getFactorial(number) {
  let factorial = 1;
  for (let i = 1; i <= number; i++) {
    factorial *= i;
  }
  return factorial;
}

function getSum(numbersToSum) {
  let sum = 0;
  numbersToSum.forEach(function (number) {
    sum += number;
  });
  return sum;
}

function multiply(numbersToMultiply) {
  let result = 1;
  numbersToMultiply.forEach(function (number) {
    result *= number;
  });
  return result;
}

function double(listToDouble) {
  return listToDouble.map((number) => number * 2)
}

module.exports = {
  getSumUntil: getSumUntil,
  getFactorial: getFactorial,
  getSum: getSum,
  multiply: multiply,
  double: double
};