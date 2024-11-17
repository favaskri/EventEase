function changeQuantity(change) {
    const quantityInput = document.getElementById('quantity');
    let currentValue = parseInt(quantityInput.value);
    let newValue = currentValue + change;

    if (newValue < parseInt(quantityInput.min)) {
        newValue = parseInt(quantityInput.min);
    } else if (newValue > parseInt(quantityInput.max)) {
        newValue = parseInt(quantityInput.max);
    }

    quantityInput.value = newValue;
}

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
    })
    .catch(error => console.error('Error:', error));
}
