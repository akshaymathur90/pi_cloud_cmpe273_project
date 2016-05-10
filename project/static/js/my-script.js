$(document).ready(function() {

    $body = $("body");
     $body.css('background-image', 'none');

    $(document).on({
        ajaxStart: function() { $body.addClass("loading"); },
        ajaxStop: function() { 
            $body.removeClass("loading");
        }
    });
    $('#btnSignUp').click(function() {
         //$body.addClass("loading"); 
        setTimeout(func, 4000);
        function func(){
            $.ajax({
                url: '/newapp',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    setTimeout(function(){}, 6000);
                    $( ".res" ).html( "<p>Application Deployed</p>" );
                    console.log(response);
                },
                error: function(error) {
                    $( ".res" ).html( "<p>Something went wrong, please check your logs</p>" );
                    console.log(error);
                }
            });
        }
    });
});
