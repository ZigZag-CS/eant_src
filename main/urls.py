"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

from apps.accounts.views import *
from apps.carts.views import *
from apps.billing.views import *
from apps.addresses.views import checkout_address_create_view, checkout_address_reuse_view, AddressListView
from apps.marketing.views import *
from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),

    # path('accounts/login/', RedirectView.as_view(url='/login')),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include("apps.accounts.urls", namespace='account')),
    path('accounts/', include("apps.accounts.passwords.urls")),

    path('address/', RedirectView.as_view(url='/addresses')),
    path('addresses/', AddressListView.as_view(), name='addresses'),

    path('contact/', contact_page, name="contact"),

    path('login/', LoginView.as_view(), name="login"),

    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),

    path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    path('logout/', LogoutView.as_view(), name="logout"),

    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('cart/', include("apps.carts.urls", namespace="carts")),

    path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
    path('billing/payment-method/create/', payment_method_createview, name='billing-payment-method-endpoint'),

    path('register/', RegisterView.as_view(), name="register"),

    path('bootstrap/', TemplateView.as_view(template_name="bootstrap/example.html")),

    path('orders/', include("apps.orders.urls", namespace='orders')),

    path('products/', include("apps.products.urls", namespace="products")),

    path('search/', include("apps.search.urls", namespace="search")),

    path('settings/', RedirectView.as_view(url='/account')),
    path('settings/email/', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    path('webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),

    # path('products/', ProductListView.as_view()),
    # # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('products/<slug:slug>/', ProductDetailSlugView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),

    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_title = "EU ... treshi la kuru meu"
admin.site.site_header = "EU ... treshi la kuru meu"
