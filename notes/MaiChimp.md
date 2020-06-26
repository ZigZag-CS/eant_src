
Mailchimp integrations:
> https://www.codingforentrepreneurs.com/blog/mailchimp-integration/


1. Tre de generat API key:
-> Accounts => Extras => API keys => Create a key

EX: 82ccf13f1459f694b1364c3e82dd8aa4-us10

2. settings.py

MAILCHIMP_API_KEY           = "82ccf13f1459f694b1364c3e82dd8aa4-us10"
MAILCHIMP_DATA_CENTER       = "us10"

+++ a treea constanta: MAILCHIMP_EMAIL_LIST_ID

=> se acceseaza https://us10.admin.mailchimp.com  " **/lists/** ""

apare lista de liste create => Settings => Audience name and default

pe pagina in "Audience ID" vedem: " ypically, this is what they want: 66dfabe12f. "

de aici luam MAILCHIMP_EMAIL_LIST_ID

si il adaugam in settings.py -> MAILCHIMP_EMAIL_LIST_ID = "66dfabe12f"

