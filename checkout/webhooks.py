from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .webhook_handler import StripeWhHandler    

import stripe


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
        print('broad exception')
        return HttpResponse(content=error, status=400)

    print(f'Success {event}!')
    return HttpResponse(status=200)
