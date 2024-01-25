$(document).ready(function() {
  console.log('hello world'); 
  $.getJSON('data.json', function(data) {
    jsonData = data;
    console.log(jsonData[0])
  })
    .done(function () {
      console.log('JSON file');
    });
});
