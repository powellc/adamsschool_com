$(document).ready(function () {
    if ($('.top_notification').hasClass('hide')) {
        $(".weather").removeClass("drop");
    } else {
        $(".weather").addClass("drop");
    };
    $(".dismiss").click(function () {
        console.log($('.top_notification').hasClass('hide'));
        $(".weather").removeClass("drop");
    });
});
$(function () {


    $('body').tooltip({
        selector: 'a[rel="tooltip"], [data-toggle="tooltip"]'
    });
});