'use strict';

const express = require('express');
const mysql = require('mysql');

const app = express();

app.use('/assets', express.static('./assets'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'licence_plates'
});

function getSortedString(stringToSort) {
  return stringToSort.split('').sort().join('');
}

function isValidInput(requestQuery) {
  let temp = requestQuery.q.replace(/[^-A-Za-z0-9]/g, '');
  return (getSortedString(requestQuery.q) === getSortedString(temp) && requestQuery.q.length <= 7);
}

function createQuery(requestQuery) {
  let myQuery = 'SELECT * FROM licence_plates WHERE plate LIKE ';
  if (requestQuery.hasOwnProperty('police') === true) {
    myQuery += `'RB%' AND plate LIKE '%${requestQuery.q}%';`;
  } else if (requestQuery.hasOwnProperty('diplomat') === true) {
    myQuery += `'DT%' AND plate LIKE '%${requestQuery.q}%';`;
  } else {
    myQuery += `'%${requestQuery.q}%';`;
  }
  return myQuery;
}

function getCarData(result) {
  let carData = [];
  result.forEach((car) => {
    carData.push({
      licence: car.plate,
      brand: car.car_brand,
      model: car.car_model,
      color: car.color,
      year: car.year
    });
  });
  return carData;
}

app.get('/search', (req, res) => {
  if (!isValidInput(req.query)) {
    res.status(400);
    res.json({
      result: "error",
      message: "invalid input"
    });
    return;
  }
  conn.query(createQuery(req.query), (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    res.status(200);
    res.json({
      result: "ok",
      data: getCarData(rows)
    });
  });  
});

app.get('/search/:brand', (req, res) => {
  let searchBrandQuery = `SELECT * FROM licence_plates WHERE car_brand = '${req.params.brand}';`;
  conn.query(searchBrandQuery, (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    res.status(200);
    res.json({
      result: "ok",
      data: getCarData(rows)
    });
  });  
});

app.listen(8080, () => {
  console.log('the app is listening.');
});
