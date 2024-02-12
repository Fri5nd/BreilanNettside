function formValidation(event){
    var usernameInput = document.getElementById("usernameInput").value;
    var passwordInput = document.getElementById("passwordInput").value;
    if(usernameInput == "" || passwordInput == "") {
        alert("Please provide both username and password")
        return false;
    } else {
        return true;
    };    
};

document.getElementById('loginForm').addEventListener('submit', function(event) {
    if(!formValidation()) {
        event.preventDefault();
    }
});