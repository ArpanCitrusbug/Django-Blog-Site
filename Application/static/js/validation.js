let emailerror = true

function emailValidation() {
    let email = $("#email").val();
    let mailformat = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (email == "") {
        $("#error-email").text("Please Enter Your Email.");
        emailerror = false;
    }
    else if(mailformat.test(email) == false) {
        $("#error-email").text("Please Enter Valid email")
        emailerror = false;
    }
    else {
        $("#error-email").text("");
        emailerror = true;
    }

}
 
$('#submit').click(function(e){
    e.preventDefault();
    emailValidation();
    if(emailerror == true) {
        return true;
    }
    else{
        return false;
    }
});