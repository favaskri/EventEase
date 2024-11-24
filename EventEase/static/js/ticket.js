

function updateTotalPrice() {
    // Retrieve the ticket price from the span element
    const ticketPriceElement = document.getElementById('ticket-price');
    const ticketPrice = parseFloat(ticketPriceElement.getAttribute('data-price'));

    // Retrieve the quantity from the input field
    const quantity = parseInt(document.getElementById('quantity').value, 10) || 1;

    // Debugging logs
    console.log("Quantity:", quantity, "Ticket Price:", ticketPrice);

    // Validate if ticketPrice is a valid number
    if (isNaN(ticketPrice)) {
        console.error("Invalid ticket price.");
        return;
    }

    // Calculate the total price
    const totalPrice = (quantity * ticketPrice).toFixed(2);
    console.log("Total Price:", totalPrice);

    // Update the total price on the page
    const totalPriceElement = document.getElementById('total-price');
    if (totalPriceElement) {
        totalPriceElement.innerText = `$${totalPrice}`;
    } else {
        console.error("Total price element not found on the page.");
    }
}



function changeQuantity(change, ticketPrice) {
    const quantityInput = document.getElementById('quantity');
    let currentValue = parseInt(quantityInput.value);
    let newValue = currentValue + change;

    // Ensure the value stays within bounds
    if (newValue < parseInt(quantityInput.min)) {
        newValue = parseInt(quantityInput.min);
    } else if (newValue > parseInt(quantityInput.max)) {
        newValue = parseInt(quantityInput.max);
    }

    quantityInput.value = newValue;

    // Call updateTotalPrice with the new quantity
    updateTotalPrice(newValue, ticketPrice);
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
        window.location.href = data.redirect_url; // Redirect to the success page
    })
    .catch(error => console.error('Error:', error));
}
