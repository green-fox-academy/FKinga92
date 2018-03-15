'use strict';

const express = require('express');
const mysql = require('mysql');

const app = express();

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'reddit'
});

app.use(express.json());
app.use('/public', express.static('./public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/main-page.html');
});

app.get('/posts', (req, res) => {
  conn.query('SELECT * FROM post;', (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    res.status(200);
    res.json({
      posts: rows
    });
  });
});

app.post('/posts', (req, res) => {
  if (req.body.hasOwnProperty('title') === 'false' || req.body.hasOwnProperty('url') === 'false') {
    res.json({ error: 'Please provide a title and an url' });
  } else {
    const newPostQuery = `INSERT INTO post (title, url, timestamp) VALUES (${conn.escape(req.body.title)},
                          ${conn.escape(req.body.url)}, ${conn.escape(req.body.timestamp)});`
    conn.query(newPostQuery, (err, results) => {
      if (err) {
        console.log(err.toString());
        res.status(500).send('Internal error');
        return;
      }
      conn.query(`SELECT * FROM post WHERE id = ${results.insertId};`, (err, rows) => {
        if (err) {
          console.log(err.toString());
          res.status(500).send('Internal error');
          return;
        }
        res.status(200);
        res.json(rows[0]);
      });
    });
  }
});

app.put('/posts/:id/upvote', (req, res) => {
  let upvoteQuery = `UPDATE post SET score = score + 1 WHERE id = ${req.params.id};`;
  conn.query(upvoteQuery, (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    conn.query(`SELECT * FROM post WHERE id = ${req.params.id};`, (err, rows) => {
      if (err) {
        console.log(err.toString());
        res.status(500).send('Internal error');
        return;
      }
      res.status(200);
      res.json(rows[0]);
    });
  });
});

app.put('/posts/:id/downvote', (req, res) => {
  let downvoteQuery = `UPDATE post SET score = score - 1 WHERE id = ${req.params.id};`;
  conn.query(downvoteQuery, (err, rows) => {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Internal error');
      return;
    }
    conn.query(`SELECT * FROM post WHERE id = ${req.params.id};`, (err, rows) => {
      if (err) {
        console.log(err.toString());
        res.status(500).send('Internal error');
        return;
      }
      res.status(200);
      res.json(rows[0]);
    });
  });
});

app.listen('3000', () => {
  console.log('the app is listening.');
});
