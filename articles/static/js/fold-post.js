// 7 лаба
document.addEventListener('DOMContentLoaded', function () {
    const foldButtons = document.querySelectorAll('.fold-button');

    foldButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const post = button.closest('.one-post');

            post.classList.toggle('folded');

            if (post.classList.contains('folded')) {
                button.textContent = 'Развернуть';
            } else {
                button.textContent = 'Свернуть';
            }
        });
    });
});