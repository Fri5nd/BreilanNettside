$(document).ready(function() {



  function validateForm(json) {
      var usernameField = $("#usernameInput").val();
      var passwordField = $("#passwordInput").val();   
      if (usernameField == json[0].username && passwordField == json[0].password) {
        $("#usernameInput, #passwordInput").val("");
        return true;
      } else {
        alert("feil brukernavn eller passord")
        $("#usernameInput, #passwordInput").val("");
        return false;
      }
  }

  function showFormEditing() {
    
  }

  $("#loginForm").submit(function(event) {
    event.preventDefault();
    $.getJSON('users.json', function(data) {
      if (validateForm(data) == true) {
        showFormEditing()
      } 
    });
  });


});
