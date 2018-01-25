'use strict';

const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use('/assets', express.static('./assets'));

app.use(bodyParser.json());

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  const input = req.query.input;
  if (input === undefined) {
    res.json(
      {
        error: 'Please provide an input!'
      }
    );
  } else {
    res.json(
      {
        received: Number(input),
        result: input * 2
      }
    );
  }
});

app.get('/greeter', function (req, res) {
  const input = req.query;
  if (input.hasOwnProperty('name') === false) {
    res.json(
      {
        error: 'Please provide a name!'
      }
    );
  } else if (input.hasOwnProperty('title') === false) {
    res.json(
      {
        error: 'Please provide a title!'
      }
    );
  } else {
    res.json(
      {
        welcome_message: `Oh, hi there ${input.name}, my dear ${input.title}!`
      }
    );
  }
});

app.get('/appenda/:appenda', function (req, res) {
  const appendable = req.params.appenda;
  res.json(
    {
      appended: `${appendable}a`
    }
  );
});

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

app.post('/dountil/:operation', function (req, res) {
  const operation = req.params.operation;
  if (req.body.hasOwnProperty('until') === false) {
    res.json(
      {
        error: 'Please provide a number!'
      }
    );
  }

  if (operation === 'sum') {
    res.json(
      {
        result: getSumUntil(req.body.until)
      }
    );
  } else if (operation === 'factor') {
    res.json(
      {
        result: getFactorial(req.body.until)
      }
  );
  }  
});

app.listen(8080, function () {
  console.log('the app is running');
});
