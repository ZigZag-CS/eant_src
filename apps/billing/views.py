from django.shortcuts import render

import stripe
# stripe.api_key = "pk_test_51GxYtbCpSvUnsz71g2FEycIhLwMXLZ39rDjn5pOSwKKjb0Qro2HjRdXO6R9xDe3OCRo7dLLoyfPRWMhX9jg6wcBO004Do4xsWQ"
stripe.api_key = "sk_test_51GxYtbCpSvUnsz716zahU925htvEVMh8fsjjZbBmsnrAPdI4Kg2VDox0AwkTKgaGFGxYW3IPEM9DtGZujqZZd5zt00iP8X27Bb"


STRIPE_PUB_KEY = 'pk_test_51GxYtbCpSvUnsz71g2FEycIhLwMXLZ39rDjn5pOSwKKjb0Qro2HjRdXO6R9xDe3OCRo7dLLoyfPRWMhX9jg6wcBO004Do4xsWQ'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})
