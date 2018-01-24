// Write a function that computes a member of the fibonacci sequence by a given index
// Create tests that covers all types of input (like in the previous workshop exercise)

const getMemberOfFibonacci = function (index) {
  if (typeof index !== 'number') {
    throw new Error(`${index} is not an integer.`);
  }
  
  if (index < 2) {
    return index;
  }
  return getMemberOfFibonacci(index - 1) + getMemberOfFibonacci(index - 2);
};

module.exports = getMemberOfFibonacci;
