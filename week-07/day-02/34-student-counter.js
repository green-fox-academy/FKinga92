'use strict';

let students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function getOwnedCandies(listToFilter) {
  let sumOfCandies = 0;
  listToFilter.forEach(function(item, index) {
    sumOfCandies += item.candies;
  })
  console.log('The students have ' + sumOfCandies + ' candies.');
}

function getSumOfAge(listToFilter) {
  let sumOfAge = 0;
  listToFilter.forEach(function(item, index) {
    (item.candies < 5) ? sumOfAge = sumOfAge + item.age : sumOfAge;
  })
  console.log('The sum of the age of the students who have less than 5 candies is ' + sumOfAge + '.');
}

getOwnedCandies(students);
getSumOfAge(students);
