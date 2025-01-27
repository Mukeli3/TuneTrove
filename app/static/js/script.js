// script.js
document.addEventListener('DOMContentLoaded', () => {
  // Navigation buttons
  const navButtons = document.querySelectorAll('.nav-btn');
  navButtons.forEach(button => {
    button.addEventListener('click', () => {
      const target = button.dataset.target;
      if (target) {
        window.location.href = target;
      }
    });
  });

  // Common error handler
  function handleError(error) {
    console.error('An error occurred:', error);
    alert('An unexpected error occurred. Please try again later.');
  }
});

