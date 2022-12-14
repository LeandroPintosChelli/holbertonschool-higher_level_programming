// JavaScript script that fetches and lists the title for all movies

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (resp) {
    let films = resp.results;
    for (let idx in films) {
      $('#list_movies').append('<li>' + films[idx].title + '</li>');
    }
  })
});
