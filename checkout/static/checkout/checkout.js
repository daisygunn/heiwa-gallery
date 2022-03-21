      // This is your test publishable API key.

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey, {locale: 'en-GB',});
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
let card = elements.create('card', {appearance: appearance});
card.mount('#payment-element');