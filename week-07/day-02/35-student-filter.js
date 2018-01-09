'use strict';

let students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

function getNameOfStudents(listToFilter) {
  let listOfStudents = '';
  listToFilter.forEach(function(item) {
    (item.candies > 4) ? listOfStudents = listOfStudents + item.name : listOfStudents;
  })
  console.log('The students who have more than 4 candies are: ' + listOfStudents + '.');
}

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function getAverageOfCandies(listToFilter) {
  let sumOfCandies = 0;
  listToFilter.forEach(function(item) {
    sumOfCandies += item.candies;
  })
  console.log('The students have ' + sumOfCandies / listToFilter.length + ' candies on average.');
}

getNameOfStudents(students);
getAverageOfCandies(students);
