#!/usr/bin/node
// Script that prints the number
// of movies where the character “Wedge Antilles” is present.

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    let movie = 0;
    for (let i = 0; i < result.length; i++) {
      const count = result[i].characteres;
      for (let j = 0; j < count.length; j++) {
        if (count[j].includes('18')) {
          movie++;
        }
      }
    }
    console.log(movie);
  }
});
