'use strict';

const express = require('express');
const mysql = require('mysql');
const app = express();

app.use('/assets', express.static('./assets'));
app.use(express.json());

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'bookstore'
});

app.get('/titles', (req, res) => {
  conn.query('SELECT book_name FROM book_mast;', (err, rows) => {
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    res.send(rows);
  });
});


app.listen(8080, () => {
  console.log('the app is listening.');
});