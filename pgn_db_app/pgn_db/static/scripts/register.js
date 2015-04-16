var username = "";
var password = "";


$('.submit').on('click',
    function(){

        user = $('.username').val();
        pass = $('.pass').val();
        if(user && pass){
            if(passwordsMatch()){

                var data = {
                    "access_token":access_token,
                    "username": user,
                    "password": pass
                };

                $.ajax({
                    type: "POST",
                    url:"/create_user",
                    data: data
                });

                }else {
                    raiseError("passwords must match");
                }
        } else {
            raiseError("no blank fields");
        }


});

var passwordsMatch = function(){
    var p1 = $('.pass').val();
    var p2 = $('.passconfirm').val();

    return p1 == p2;
};

var raiseError = function(text){
    alert(text);
};