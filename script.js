$(document).ready(function() {
  let jsonData;
  $.getJSON('users.json', function(data) {
    jsonData = data;
  });
  console.log(jsonData[0])  
  function validateForm() {
    var usernameField = $("#usernameInput").val();
    var passwordField = $("#passwordInput").val();   
    $.getJSON('users.json', function(data) {
      jsonData = data;
    });
    console.log(jsonData[0])
    // if(jsonData[0].username == usernameField && jsonData[0].password == passwordField) {
    //   console.log("Yay!")
    // } else {
    //   alert("Feil brukernavn eller passord")
    // }

  }
  
  $("#loginForm").submit(function(event) {
    event.preventDefault();
    validateForm();
  });


});
