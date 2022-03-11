$(document).ready(function() {

    var i = setInterval(function ()
      {
          console.log("Getting user submit ")
          if ($(".user_submit").length)
          {
              clearInterval(i);
              $(".user_submit").each(function (event) {
                $(this).on('click',  function(event){
                    submit_action("user_submit")
                })
              });
          }
      }, 100);
});


function submit_action(event) {
    console.log("action:", event)
    alert(event)
}

