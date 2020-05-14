$(document).ready(function() {
    $("#do_login").click(function() { 
       closeLoginInfo();
       $(this).parent().find('span').css("display","none");
       $(this).parent().find('span').removeClass("i-save");
       $(this).parent().find('span').removeClass("i-warning");
       $(this).parent().find('span').removeClass("i-close");
       
        var proceed = true;
        $("#login_form input").each(function(){
            
            if(!$.trim($(this).val())){
                $(this).parent().find('span').addClass("i-warning");
            	$(this).parent().find('span').css("display","block");  
                proceed = false;
            }
        });
       
        if(proceed) //everything looks good! proceed...
        {
            $(this).parent().find('span').addClass("i-save");
            $(this).parent().find('span').css("display","block");
        }
    });
    
    //reset previously results and hide all message on .keyup()
    $("#login_form input").keyup(function() { 
        $(this).parent().find('span').css("display","none");
    });
 
});

