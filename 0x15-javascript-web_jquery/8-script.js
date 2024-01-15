$(document).ready(function () {
  (async () => {
    try {
      const movies = await getIt();
      movies.forEach(el => {
        $('UL#list_movies').append('<li>' + el + '</li>');
      });
    } catch (e) {
      console.error(e);
    }
  })();
});

async function getIt () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  const res = await fetch(url);
  const movies = [];
  if (res.ok) {
    const data = await res.json();
    data.results.forEach(el => {
      movies.push(el.title);
    });
    return movies;
  }
  console.error('Error:', res.statusText);
  throw new Error('Failed to fetch data');
}
