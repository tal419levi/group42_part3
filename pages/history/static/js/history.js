document.addEventListener('DOMContentLoaded', () => {
    const lessons = document.querySelectorAll('.lesson');

    lessons.forEach(lesson => {
        lesson.addEventListener('mouseover', () => {
            lesson.style.backgroundColor = 'lightgray';
        });

        lesson.addEventListener('mouseout', () => {
            lesson.style.backgroundColor = '';
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.button');

    buttons.forEach(button => {
        button.addEventListener('click', (event) => {
            if (event.target.classList.contains('button')) {
                window.location.href = 'Feedback';
            }
        });
    });
});
