#!/usr/bin/node
// Script that prints the number
// of movies where the character “Wedge Antilles” is present.

const request = require('request');
let films = 0;
let url = process.argv[2]

request(url, function (error, response, body) {
  if (error == null) {
    const completed = JSON.parse(body);
    const results = completed.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          films++;
        }
      }
    }
  }
  console.log(films);
});
