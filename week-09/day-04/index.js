'use strict';

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const math = require('./operations');

app.use('/assets', express.static('./assets'));

app.use(bodyParser.json());

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  const input = req.query.input;
  if (input === undefined) {
    res.json({ error: 'Please provide an input!' });
  } else {
    res.json({
        received: Number(input),
        result: input * 2
    });
  }
});

app.get('/greeter', function (req, res) {
  const input = req.query;
  if (input.hasOwnProperty('name') === false) {
    res.json({ error: 'Please provide a name!' });
  } else if (input.hasOwnProperty('title') === false) {
    res.json({ error: 'Please provide a title!' });
  } else {
    res.json({ welcome_message: `Oh, hi there ${input.name}, my dear ${input.title}!` });
  }
});

app.get('/appenda/:appenda', function (req, res) {
  const appendable = req.params.appenda;
  res.json({ appended: `${appendable}a` });
});

app.post('/dountil/:operation', function (req, res) {
  const operation = req.params.operation;
  if (req.body.hasOwnProperty('until') === false) {
    res.json({ error: 'Please provide a number!' });
  } else if (operation === 'sum') {
    res.json({ result: math.getSumUntil(req.body.until) });
  } else if (operation === 'factor') {
    res.json({ result: math.getFactorial(req.body.until) });
  }  
});

app.post('/arrays', function (req, res) {
  const operation = req.body.what;
  if (req.body.hasOwnProperty('what') === false) {
    res.json({ error: 'Please provide what to do with the numbers!' });
  } else if (req.body.hasOwnProperty('numbers') === false) {
    res.json({ error: 'Please provide numbers!' });
  } else if(operation === 'sum') {
    res.json({ result: math.getSum(req.body.numbers) });
  } else if (operation === 'multiply') {
    res.json({ result: math.multiply(req.body.numbers) });
  } else if (operation === 'double') {
    res.json({ result: math.double(req.body.numbers) });
  }
});

app.listen(8080, function () {
  console.log('the app is running');
});
