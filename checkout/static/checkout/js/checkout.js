/*jshint esversion: 6 */
/*globals $, Stripe */

// If save address box is ticked then add or remove checked attribute
$('#save-address').click(function () {
    if ($(this).attr('checked')) {
        $(this).removeAttr('checked');
    } else {
        $(this).attr('checked', 'checked');
    }
});

// https://stripe.com/docs/payments/accept-a-payment

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey, {
    locale: 'en-GB',
});
let elements = stripe.elements();

const appearance = {
    theme: 'stripe',
    variables: {
        fontFamily: 'Josefin Sans, sans-serif',
        colorBackground: '#ffffff',
        colorDanger: '#df1b41',
        spacingUnit: '2px',
        borderRadius: '4px',
    },
    rules: {
        '.Tab': {
            border: '1px solid #E0E6EB',
            boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02)',
        },

        '.Tab:hover': {
            color: 'var(--colorText)',
        },

        '.Tab--selected': {
            borderColor: '#E0E6EB',
            boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02), 0 0 0 2px var(--colorPrimary)',
        },

        '.Input--invalid': {
            boxShadow: '0 1px 1px 0 rgba(0, 0, 0, 0.07), 0 0 0 2px var(--colorDanger)',
        },

        // See all supported class names and selector syntax below
    }
};

// Create an instance of the card Element
let card = elements.create('card', {
    appearance: appearance
});
card.mount('#payment-element');

card.addEventListener('change', function (event) {
    if (event.error) {
        showMessage(`${event.error.message}`);
    }
});

var form = document.getElementById('stripe-payment-form');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    setLoading(true);
    var saveAddress = Boolean($('#save-address').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_address': saveAddress,
    };
    var url = '/checkout/cache_checkout_data';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.flat_house.value),
                        line2: $.trim(form.street_address.value),
                        city: $.trim(form.town_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.flat_house.value),
                    line2: $.trim(form.street_address.value),
                    city: $.trim(form.town_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                showMessage(`${result.error.message}`);
                setLoading(false);
            } else {
                if (result.paymentIntent.status == 'succeeded') {
                    showMessage("Payment succeeded!");
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });
});

// ------- UI helpers -------

function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;

    setTimeout(function () {
        messageContainer.classList.add("hidden");
        messageText.textContent = "";
    }, 6000);
}

// Show a spinner on payment submission
function setLoading(isLoading) {
    if (isLoading) {
        // Disable the button and show a spinner
        document.querySelector("#payment-submit-button").disabled = true;
        document.querySelector("#spinner").classList.remove("hidden");
        document.querySelector("#button-text").classList.add("hidden");
    } else {
        document.querySelector("#payment-submit-button").disabled = false;
        document.querySelector("#spinner").classList.add("hidden");
        document.querySelector("#button-text").classList.remove("hidden");
    }
}