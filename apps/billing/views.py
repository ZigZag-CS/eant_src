from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

import stripe

# stripe.api_key = "pk_test_51GxYtbCpSvUnsz71g2FEycIhLwMXLZ39rDjn5pOSwKKjb0Qro2HjRdXO6R9xDe3OCRo7dLLoyfPRWMhX9jg6wcBO004Do4xsWQ"
stripe.api_key = "sk_test_51GxYtbCpSvUnsz716zahU925htvEVMh8fsjjZbBmsnrAPdI4Kg2VDox0AwkTKgaGFGxYW3IPEM9DtGZujqZZd5zt00iP8X27Bb"


STRIPE_PUB_KEY = 'pk_test_51GxYtbCpSvUnsz71g2FEycIhLwMXLZ39rDjn5pOSwKKjb0Qro2HjRdXO6R9xDe3OCRo7dLLoyfPRWMhX9jg6wcBO004Do4xsWQ'


def payment_method_view(request):
    #next_url =
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})




def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        print(request.POST)
        return JsonResponse({"message": "Done"})
    return HttpResponse("error", status_code=401)