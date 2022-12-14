#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (!error) {
    const completed = {};
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (completed[todos[i].userId] === undefined) {
          completed[todos[i].userId] = 0;
        }
        completed[todos[i].userId]++;
      }
    }
    console.log(completed);
  }
});
