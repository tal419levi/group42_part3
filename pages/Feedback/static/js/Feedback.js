document.addEventListener('DOMContentLoaded', () => {
    const feedbackTextarea = document.getElementById('feedback');
    const ratingSelect = document.getElementById('rating');
    const submitFeedbackBtn = document.getElementById('submit_feedback');

    submitFeedbackBtn.addEventListener('click', (event) => {
        const feedbackText = feedbackTextarea.value.trim();
        const selectedRating = ratingSelect.value;

        if (!feedbackText || selectedRating === 'בחר') {
            // Prevent form submission if feedback or rating is empty
            event.preventDefault();
            alert('אנא מלא את הטופס');
        } else {
            alert('הערכה נשלחה, תודה רבה!');
            // Form submission will proceed as usual
        }
    });

    // Add event for the "חזור" button
    const historyBtn = document.querySelector('.history-btn');
    if (historyBtn) {
        historyBtn.addEventListener('click', () => {
            window.location.href = 'history.html';
        });
    }
});
