$(".stars").mousemove(function(e) {
    var gLeft = $(".stars .stars-ghost").offset().left,
    px = e.pageX;

    $(".stars .stars-ghost").width(pX - gLeft);

});