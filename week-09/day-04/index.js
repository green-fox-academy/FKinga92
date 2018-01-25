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
    res.json({received: input, result: input * 2});
  }
});

app.listen(8080, function () {
  console.log('the app is running');
});
