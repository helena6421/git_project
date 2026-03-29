// 8 лаба
$(document).ready(function () {
    $('.one-post').hover(
        function () {
            $(this).find('.one-post-shadow').stop().animate({ opacity: 0.1 }, 300);
        },
        function () {
            $(this).find('.one-post-shadow').stop().animate({ opacity: 0 }, 300);
        }
    );
});