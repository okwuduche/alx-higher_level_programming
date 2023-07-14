#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const id = args[0];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
