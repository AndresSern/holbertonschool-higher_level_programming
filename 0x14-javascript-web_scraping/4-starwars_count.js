#!/usr/bin/node
/*
 * Script that prints the number of movies where the character "Wedge Antilles"
 * is present
*/

const url = 'https://swapi-api.hbtn.io/api/films';
const request = require('request');

request(url, function (err, result, body) {
  const films = body;
  const ocurrencesFilms = films.split('https://swapi-api.hbtn.io/api/people/18/').length - 1;
  console.log(ocurrencesFilms);
  if (err) {
    console.log(err);
  }
});
