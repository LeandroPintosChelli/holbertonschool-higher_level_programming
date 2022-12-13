#!/usr/bin/node
// Script that prints the title of
// a Star Wars movie where the episode number matches a given integer.

const id = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
