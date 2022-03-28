from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe
from .webhook_handler import StripeWhHandler


# https://stripe.com/docs/payments/handling-payment-events
@require_POST
@csrf_exempt
def webhook(request):
    """ webhook """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret)
    except ValueError as error:
        return HttpResponse(content=error, status=400)
    except stripe.error.SignatureVerificationError as error:
        return HttpResponse(content=error, status=400)
    except Exception as error:
        return HttpResponse(content=error, status=400)

    # set up to use webhook handler
    handler = StripeWhHandler(request)

    # map webhooks to relevant handle function
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
        handler.handle_payment_intent_payment_failed,
    }

    # get the webhook type from Stripe
    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)

    # call the event handler with the event
    response = event_handler(event)
    return response
