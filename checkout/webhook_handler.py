from django.http import HttpResponse


class StripeWhHandler:
    """ handle all stripe webhooks """
    def __init__(self, request):
        """ init method """
        self.request = request

    def handle_event(self, event):
        """ handle all generic events """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ handle all successful events """
        return HttpResponse(
            content=f"webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ handle all unsuccessful events """
        return HttpResponse(
            content=f"webhook received: {event['type']}",
            status=200)
