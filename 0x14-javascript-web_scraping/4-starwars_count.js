#!/usr/bin/node
/*
 * Script that prints the number of movies where the character "Wedge Antilles"
 * is present
*/

const url = 'https://swapi-api.hbtn.io/api/films';
const request = require('request');

request(url, function (err, result, body) {
  const films = body;
  const countFilms = films.split('https://swapi-api.hbtn.io/api/people/18/').length - 1;
  countFilms === -1 ? console.log(0) : console.log(countFilms);
  if (err) {
    console.log(err);
  }
});
