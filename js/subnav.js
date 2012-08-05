$(document).scroll(function(){
    $masthead = $('#masthead button')
    masthead_bottom = $masthead.offset().top
    if ($(this).scrollTop() > masthead_bottom) {
        $('#global-nav button').removeClass('btn-inverse');
        $('#global-nav button').addClass('btn-primary');
    } else {
        $('#global-nav button').removeClass('btn-primary');
        $('#global-nav button').addClass('btn-inverse');
    }
});


$('#global-nav').scrollspy()
