// $(document).ready(function() {
$( "#target" ).click(function() {
    $(".order:last").clone(true).appendTo(".wrapper");        
   
});

$(".glyphicon-remove").click(function () {
    var numItems = $('.order').length;
   
    if(numItems != 1) {
        $(this).closest(".order").remove();
    }
});