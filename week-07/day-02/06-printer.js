'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(inputToLog) {
  console.log(Object.values(arguments).join(', '));
}

printer('fa');
printer('kutya', 'fa', 'alma', 4, true);
