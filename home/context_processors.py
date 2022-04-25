from django.conf import settings
# import mailchimp_marketing as MailchimpMarketing
from mailchimp3 import MailChimp
from mailchimp_marketing.api_client import ApiClientError


def get_newsletter_emails(request):
    try:
        client = MailChimp(
            mc_api=settings.MAILCHIMP_API_KEY, mc_user=settings.MC_USER)

        response = client.lists.members.all(
            "a9f944f3e8", fields="members.email_address", offset=0)

        email_list = []
        for x in response.values():
            for y in x:
                list_emails = (list(y.values()))
                for a in list_emails:
                    email_list.append(a)

    except ApiClientError as error:
        print("Error: {}".format(error.text))
        response = ""
        email_list = []

    context = {
        'email_list': email_list,
    }

    return context
