'use strict';

const express = require('express');
const app = express();

app.use('/assets', express.static('./assets'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  const input = req.query.input;
  if (input === undefined) {
    res.json({error: 'Please provide an input!'});
  } else {
    res.json({received: Number(input), result: input * 2});
  }
});

app.get('/greeter', function (req, res) {
  const input = req.query;
  if (input.hasOwnProperty('name') === false) {
    res.json({
      error: 'Please provide a name!'
    });
  } else if (input.hasOwnProperty('title') === false) {
    res.json({
      error: 'Please provide a title!'
    });
  } else {
    res.json({
      welcome_message: `Oh, hi there ${input.name}, my dear ${input.title}!`
    });
  }
});

app.get('/appenda/:appenda', function (req, res) {
  const appendable = req.params.appenda;
  res.json({
    appended: `${appendable}a`
  });
});

app.listen(8080, function () {
  console.log('the app is running');
});
