document.addEventListener('DOMContentLoaded', () => {
  // Login functionality
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ email, password }),
      })
      .then(response => {
        if (response.ok) {
          return response.json(); // extract token
        } else {
          return response.json().then(data => {
            throw new Error(data.error || 'Login failed');
          });
        }
      })
      .then(data => {
        console.log('JWT Token:', data.token);
        sessionStorage.setItem('jwt', data.token); // Store JWT in session storage
        navigateToDashboard(); // Redirect to dashboard
      })
      .catch(error => console.error('Login error:', error));
    });
  }

  // Navigation to the dashboard
  const navigateToDashboard = () => {
    const token = sessionStorage.getItem('jwt');
    if (!token) {
      console.error('JWT token not found in session storage');
      alert('JWT token not found. Please log in again.');
      return;
    }

    console.log(`Authorization Header: Bearer ${token}`);

    fetch('/dashboard', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    .then(response => {
      if (response.ok) {
        window.location.href = '/dashboard';
      } else {
        response.json().then(data => {
          console.error('Dashboard access denied:', data);
          alert('Access denied. Please log in again.');
        });
      }
    })
    .catch(error => console.error('Navigation error:', error));
  }

  // Registration functionality
  const registerForm = document.getElementById('register-form');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const formData = new FormData(registerForm);

      fetch('/register', {
        method: 'POST',
        body: formData,
      })
        .then(response => {
          if (response.ok) {
            alert('Registration successful! Redirecting to login...');
            window.location.href = '/login';
          } else {
            alert('Registration failed. Please try again.');
          }
        })
        .catch(error => console.error('Registration error:', error));
    });
  }

  // Logout functionality
  const logoutButton = document.getElementById('logout-btn');
  if (logoutButton) {
    logoutButton.addEventListener('click', () => {
      fetch('/logout', { method: 'POST' })
        .then(response => {
          if (response.ok) {
            window.location.href = '/';
          }
        })
        .catch(error => console.error('Logout error:', error));
    });
  }
});
