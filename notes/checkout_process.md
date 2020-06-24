LINKS:
> https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
> https://www.codingforentrepreneurs.com/blog/custom-analytics-with-django/#watch
Stripe API
> https://stripe.com/docs/payments
> https://stripe.com/docs/payments/accept-a-payment-charges#web




Checkout Process

1. Cart -> Checkout View
?
- login/register or enter email (as guest)
- shipping adress
- billing info
-- billing adress
-- credit card / payment

2. Billing app/component
- billing profile
-- user or email(guest email)
-- generating payment processor token (stripe or braintree)

3. Orders / Invoices component
- connecting the billing profile
- shiping . biling adress
- cart
- status -- shipped? Canceled?

4.1. Backup Fixtures
python manage.py dumpdata products --format json  --indent 4 > apps/products/fixtures/products.json

4.2. Restore from Fixtures
python manage.py loaddata apps/products/fixtures/products.json