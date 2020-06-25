from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import BillingProfile, Card

import stripe

STRIPE_SECRET_KEY = getattr(settings, 'STRIPE_SECRET_KEY', 'sk_test_51Gxu7mBgsgm0vdRS0V3qyVq8CmdM7ZW13BYNylWjlfyyAGKPLfpoZcQAKzePNZcqYgMn6aBeG0pVMfl7VWiPwX9X00yQRBPTah')
STRIPE_PUB_KEY = getattr(settings, 'STRIPE_PUB_KEY', 'pk_test_51Gxu7mBgsgm0vdRSpZaF0ImDWNJH9ZW1d0lHyzo9KiHSPxkvktfStGLDMDvgtbKzuFAjitgFUoLvUhSGL122yE0Y00fSOJwl2M')
stripe.api_key = STRIPE_SECRET_KEY


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
            new_card_obj = Card.objects.add_new(billing_profile, token)
            # customer = stripe.Customer.retrieve(billing_profile.customer_id)
            # card_response = customer.sources.create(source=token)
            # new_card_obj = Card.objects.add_new(billing_profile, card_response)
            # print(new_card_obj)  # start saving our cards too!
        return JsonResponse({"message": "Success! Your card was adaugata!"})
    return HttpResponse("error", status_code=401)