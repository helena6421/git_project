$(document).ready(function () {
    $(window).on('scroll', function () {
        let scroll = $(window).scrollTop();

        $('.layer1').css('transform', 'translateY(' + scroll * 0.2 + 'px)');
        $('.layer2').css('transform', 'translateY(' + scroll * 0.1 + 'px)');
        $('.layer3').css('transform', 'translateY(' + scroll * 0.05 + 'px)');
    });
});