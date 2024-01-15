$(document).ready(function () {
  (async () => {
    const val = await getIt();
    $('DIV#hello').text(val);
  })();
});

async function getIt () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const res = await fetch(url);
  if (res.ok) {
    const data = await res.json();
    return data.hello;
  }
  console.error('Error:', res.statusText);
  throw new Error('Failed to fetch data');
}
