from django.conf import settings
from mailchimp3 import MailChimp
from mailchimp_marketing.api_client import ApiClientError


def get_newsletter_emails(request):
    """ get list of emails that have registered for the newsletter """
    try:
        client = MailChimp(
            mc_api=settings.MAILCHIMP_API_KEY, mc_user=settings.MC_USER)
        # get the emails from the list
        response = client.lists.members.all(
            "a9f944f3e8", fields="members.email_address", offset=0)
        # create empty list
        email_list = []
        # get the values from the response
        for x in response.values():
            for y in x:
                list_emails = (list(y.values()))
                for a in list_emails:
                    # append each email to the list
                    email_list.append(a)

    except ApiClientError as error:
        print("Error: {}".format(error.text))
        response = ""
        email_list = []

    context = {
        'email_list': email_list,
    }

    return context
