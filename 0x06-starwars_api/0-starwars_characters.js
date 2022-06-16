#!/usr/bin/node

/**
*Write a script that prints all characters of
*a Star Wars movie:

*The first positional argument passed is the
*Movie ID - example: 3 = “Return of the Jedi”
*Display one character name per line in the
*same order as the “characters” list in the
*`/films/` endpoint
*You must use the Star wars API
*You must use the request module
*/

const request = require('request');

const film_num = process.argv[2] + '/';
const film_url = 'https://swapi-api.hbtn.io/api/films/';

request(film_url + film_num, async function (err, res, body) {
    if (err) return console.error(err);
    const char_list = JSON.parse(body).characters;

    for (const charURL of char_list) {
	await new Promise(function (resolve, reject) {
	    request(charURL, function (err, res, body) {
		if (err) return console.error(err);
		console.log(JSON.parse(body).name);
		resolve();
	    });
	});
    }
});
