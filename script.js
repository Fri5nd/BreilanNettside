$(document).ready(function() {
  let jsonData = {};
  $.getJSON('users.json', function(data) {
    validateForm(data)
  });

  function validateForm(json) {
    var usernameField = $("#usernameInput").val();
    var passwordField = $("#passwordInput").val();   
    
  }
  
  $("#loginForm").submit(function(event) {
    event.preventDefault();
    validateForm();
  });
});
