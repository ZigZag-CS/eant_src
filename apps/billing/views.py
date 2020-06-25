from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import BillingProfile, Card

import stripe

# stripe.api_key = "pk_test_51GxYtbCpSvUnsz71g2FEycIhLwMXLZ39rDjn5pOSwKKjb0Qro2HjRdXO6R9xDe3OCRo7dLLoyfPRWMhX9jg6wcBO004Do4xsWQ"
stripe.api_key = "sk_test_51GxYtbCpSvUnsz716zahU925htvEVMh8fsjjZbBmsnrAPdI4Kg2VDox0AwkTKgaGFGxYW3IPEM9DtGZujqZZd5zt00iP8X27Bb"


STRIPE_PUB_KEY = 'pk_test_51GxYtbCpSvUnsz71g2FEycIhLwMXLZ39rDjn5pOSwKKjb0Qro2HjRdXO6R9xDe3OCRo7dLLoyfPRWMhX9jg6wcBO004Do4xsWQ'


def payment_method_view(request):
    #next_url =
    # next_url = None
    # next_ = request.GET.get('next')
    # if is_safe_url(next_, request.get_host()):
    #     next_url = next_

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})



def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        # print(request.POST)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this luser"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            card_response = customer.sources.create(source=token)
            new_card_obj = Card.objects.add_new(billing_profile, card_response)
            print(new_card_obj)  # start saving our cards too!
        return JsonResponse({"message": "Success! Your card was adaugata!"})
    return HttpResponse("error", status_code=401)