$(document).ready(function() {
  console.log('hello world'); 
  $.getJSON('users.json', function(data) {
    jsonData = data;
    console.log(jsonData[0])
  })
    .done(function () {
      console.log('JSON file');
    });
});
