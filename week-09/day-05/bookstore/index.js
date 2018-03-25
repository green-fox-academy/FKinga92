'use strict';

const express = require('express');
const mysql = require('mysql');
const path = require('path');
const app = express();

app.use('/assets', express.static('./assets'));

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'bookstore'
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/index.html'));
});

app.get('/titles', (req, res) => {
  conn.query('SELECT book_name FROM book_mast;', (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    res.status(200);
    res.json(rows);
  });
});

app.get('/books', (req, res) => {
  const requestQuery = req.query;
  let myQuery = 'SELECT book_name, aut_name, cate_descrip, pub_name, book_price ' +
                'FROM book_mast ' +
                'INNER JOIN author ON book_mast.aut_id = author.aut_id ' +
                'INNER JOIN category ON book_mast.cate_id = category.cate_id ' +
                'INNER JOIN newpublisher ON book_mast.pub_id = newpublisher.pub_id ';
  
  if (Object.keys(requestQuery).length > 0) {
    myQuery += 'WHERE ' + [
      ['category', `cate_descrip LIKE "%${requestQuery.category}%"`],
      ['publisher', `pub_name LIKE "%${requestQuery.publisher}%"`],
      ['plt', `book_price < ${conn.escape(requestQuery.plt)}`],
      ['pgt', `book_price > ${conn.escape(requestQuery.pgt)}`]
    ]
    .filter((propertyName) => requestQuery.hasOwnProperty(propertyName[0]))
    .map((nameValuePair) => nameValuePair[1])
    .join(' AND ') + ';';
  }

  conn.query(myQuery, (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    res.status(200);
    res.json(rows);
  });
});

app.listen(8080, () => console.log('the app is listening.'));
