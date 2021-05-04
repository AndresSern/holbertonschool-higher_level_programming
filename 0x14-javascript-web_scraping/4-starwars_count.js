#!/usr/bin/node
/*
 * Script that prints the number of movies where the character "Wedge Antilles"
 * is present
*/
const url = 'https://swapi-api.hbtn.io/api/films';
const request = require('request');

request(url, function (err, result, body) {
  const films = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < films.length; i++){
    tempCount = films[i].characters.toString().match(/people\/18/g);
    if(tempCount !== null){
       count = count + tempCount.length;
    }
  }
  console.log(count);
  if (err) {
  }
});
