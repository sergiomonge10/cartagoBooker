jQuery(document).ready(function() {
       $("#test").submit(function(event){
       event.preventDefault();
            $.ajax({
                 type:"GET",
                 url:"/tienda4g/cart",
                 data: {
                        'video': $('#test').val() // from form
                        },
                 success: function(){
                     $('#message').html("<h2>Contact Form Submitted!</h2>")
                      
                    }
            });
            return false;
       });

    });