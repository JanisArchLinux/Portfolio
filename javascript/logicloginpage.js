// logicloginpage.js

// Define a simple admin username and password for demonstration purposes.
const adminUsername = "admin";
const adminPassword = "+*v8Vd=IjGGH2NeH)5wl";

function login() {
  // Get the input values.
  const usernameInput = document.getElementById("username").value;
  const passwordInput = document.getElementById("password").value;

  // Check if the entered username and password match the admin credentials.
  if (usernameInput === adminUsername && passwordInput === adminPassword) {
    // Successful login, redirect to the admin panel or desired page.
    alert("Login successful! Redirecting to admin panel...");
    window.location.href = "Pages/page.html"; // Replace with your admin panel URL.
  } else {
    // Display an error message for invalid credentials.
    alert("Invalid username or password. Please try again.");
  }
}
