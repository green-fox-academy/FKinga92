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
  database: 'warehouse'
});

app.get('/warehouse', (req, res) => {
  const myQuery = 'SELECT id, item_name, manufacturer, category, size, unit_price FROM warehouse;';
  conn.query(myQuery, (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    res.status(200);
    res.json({
      result: 'ok',
      clothes: rows
    });
  });
});

function getOrderQuery(requestQuery) {
  return `SELECT unit_price FROM warehouse
          WHERE item_name = '${requestQuery.item}'
          AND size = '${requestQuery.size}'
          AND in_store >= ${conn.escape(requestQuery.quantity)};`;
}

app.get('/price-check', (req, res) => {
  if (req.query.quantity < 3) {
    res.status(400);
    res.json({ result: 'Please order at least 3, one for yourself, two for your friends' });
    return;
  }
  conn.query(getOrderQuery(req.query), (err, result) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    if (result[0] === undefined) {
      res.status(400);
      res.json({ result: 'Error, we don\'t have enough items in store' });
      return;
    }
    res.status(200);
    res.json({
      result: 'ok',
      total_price: result[0]['unit_price'] * req.query.quantity
    });
  });
});

app.listen(8080, () => {
  console.log('the app is listening.');
});
