import hashlib
import json
import re
import requests
from django.conf import settings



MAILCHIMP_API_KEY = getattr(settings, "MAILCHIMP_API_KEY", None)
MAILCHIMP_DATA_CENTER = getattr(settings, "MAILCHIMP_DATA_CENTER", None)
MAILCHIMP_EMAIL_LIST_ID = getattr(settings, "MAILCHIMP_EMAIL_LIST_ID", None)


def check_email(email):
    if not re.match(r".+@.+\..+", email):
        raise ValueError('String passed is not a valid email address')
    return email


def get_subscriber_hash(member_email):
    check_email(member_email)
    member_email = member_email.lower().encode()
    m = hashlib.md5(member_email)
    return m.hexdigest()


class Mailchimp(object):

    def __init__(self):
        super(Mailchimp, self).__init__()
        self.key = MAILCHIMP_API_KEY
        self.api_url = f"https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0"
        # self.api_url = "https://{dc}.api.mailchimp.com/3.0".format(dc=MAILCHIMP_DATA_CENTER)
        self.list_id = MAILCHIMP_EMAIL_LIST_ID
        # self.list_endpoint = '{api_url}/lists/{list_id}'.format(api_url=self.api_url, list_id=self.list_id)
        self.list_endpoint = f"{self.api_url}/lists/{self.list_id}"


    def get_members_endpoint(self):
        # print("in get_members_endpoint")
        print(self.list_endpoint)
        return self.list_endpoint + "/members"


    def change_subcription_status(self, email, status='unsubscribed'):
        hashed_email = get_subscriber_hash(email)
        endpoint = self.get_members_endpoint() + "/" + hashed_email
        # print(f'in change_subcription_status, endpoint= {endpoint}')
        data = {
            "email_address": email,
            "status": self.check_valid_status(status)
        }
        r = requests.put(endpoint, auth=("", self.key), data=json.dumps(data))
        # print(f' r status = {r.status_code}')
        return r.status_code, r.json()


    def check_subcription_status(self, email):
        hashed_email = get_subscriber_hash(email)
        endpoint = self.get_members_endpoint() + "/" +  hashed_email
        r = requests.get(endpoint, auth=("", self.key))
        return r.status_code, r.json()


    def check_valid_status(self, status):
        choices = ['subscribed', 'unsubscribed', 'cleaned', 'pending']
        if status not in choices:
            raise ValueError("Not a valid choice for email status")
        return status


    def add_email(self, email):
        # status = "subscribed"
        # self.check_valid_status(status)
        # data = {
        #     "email_address": email,
        #     "status": status
        # }
        # endpoint = self.list_endpoint + "/members"
        # r = requests.post(
        #     endpoint,
        #     auth=("", self.key),
        #     data=json.dumps(data)
        # )
        return self.change_subcription_status(email, status='subscribed')

    def add_email1(self, email):
        status = "subscribed"
        self.check_valid_status(status)
        data = {
            "email_address": email,
            "status": status
        }
        endpoint = self.list_endpoint + "/members"
        # print(f"add_email1 endpoint = {endpoint}")
        r = requests.post(
            endpoint,
            auth=("", self.key),
            data=json.dumps(data)
        )
        # print(f"add_email1 r = {r}")
        return r.json()

    def unsubscribe(self, email):
        return self.change_subcription_status(email, status='unsubscribed')

    def subscribe(self, email):
        return self.change_subcription_status(email, status='subscribed')

    def pending(self, email):
        return self.change_subcription_status(email, status='pending')