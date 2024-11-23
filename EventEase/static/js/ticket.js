function submitForm() {
    const form = document.getElementById('ticket-form');
    const formData = new FormData(form);
    const url = form.action;

    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
        }
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                alert(data.error || 'An error occurred.');
                throw new Error('Request failed');
            });
        }
        return response.json();
    })
    .then(data => {
        alert(`Tickets purchased: ${data.quantity}\nTotal amount: $${data.total_price}`);
        window.location.href = data.redirect_url; // Redirect to the success page
    })
    .catch(error => console.error('Error:', error));
}
