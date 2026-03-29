// 8 лаба
$(document).ready(function () {
    $('.blog-logo').hover(
        function () {
            $(this).css('transform', 'scale(1.2)');
        },
        function () {
            $(this).css('transform', 'scale(1)');
        }
    );
});