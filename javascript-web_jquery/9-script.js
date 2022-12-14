// JavaScript script that fetches and displays 
// the value of hello from that fetch in the HTML tag

$(() => {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
    $('div#hello').text(data.hello);
  });
});
