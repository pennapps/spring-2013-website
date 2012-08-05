$MASTHEAD = $('#masthead button');

if ($MASTHEAD.length === 0) {
    $('#global-nav button').removeClass('btn-inverse');
    $('#global-nav button').addClass('btn-primary');
} else {
    $(document).scroll(function(){
        masthead_bottom = $MASTHEAD.offset().top
        if ($(this).scrollTop() > masthead_bottom) {
            $('#global-nav button').removeClass('btn-inverse');
            $('#global-nav button').addClass('btn-primary');
        } else {
            $('#global-nav button').removeClass('btn-primary');
            $('#global-nav button').addClass('btn-inverse');
        }
    });
}


$('#global-nav').scrollspy()
