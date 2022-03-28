from django.http import HttpResponse


class StripeWh_Handler:
    """ handle all stripe webhooks """
    def __init__(self, request):
        """ init method """
        self.request = request

    def handle_event(self, event):
        """ handle all events """
        return HttpResponse(
            content=f"webhook received: {event['type']}",
            status=200)
