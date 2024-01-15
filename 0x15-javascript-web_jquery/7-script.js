$(document).ready(function () {
  (async () => {
    try {
      const val = await checkName();
      $('DIV#character').text(val);
    } catch (e) {
      console.error(e);
    }
  })();
});

async function checkName () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  const res = await fetch(url);
  if (res.ok) {
    const data = await res.json();
    return data.name;
  }
  console.error('Error:', res.statusText);
  throw new Error('Failed to fetch data');
}
