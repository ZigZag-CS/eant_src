"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's&$$9m9mmxja2a43i4-by+i$i1y@=-z&b(=hv=+x*neb#2c)eo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # project apps
    'apps.products.apps.ProductsConfig',
    'apps.search.apps.SearchConfig',
    'apps.tags.apps.TagsConfig',
    'apps.carts.apps.CartsConfig',
    'apps.orders.apps.OrdersConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.billing.apps.BillingConfig',
    'apps.addresses.apps.AddressesConfig',
    'apps.analytics.apps.AnalyticsConfig',
    'apps.marketing.apps.MarketingConfig',

]

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'


# ######## GMAIL settings ################

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'ps96068@gmail.com'
# EMAIL_HOST_PASSWORD = '!@'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = "Eant - src <ps96068@gmail.com>"
# BASE_URL = "http://127.0.0.1:8000"
#
# MANAGERS = (
#     ("Stefan Popa", "ps96068@gmail.com" ),
# )
#
# ADMINS = MANAGERS

# ######## END GMAIL settings ################

# ######## SENDGRID settings ################

SENDGRID_API_KEY = SENDGRID_API_KEY = 'mfDjFmsdEA7zkrcsU'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Eant - src <ps96068@gmail.com>"

# ######## END SENDGRID settings ################

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION= False

# ######## MAILCHIMP settings ################

# MAILCHIMP_API_KEY           = "f278d3c1cd861d90f0fd6119d24f35f5-us10"
# MAILCHIMP_DATA_CENTER       = "us10"
# MAILCHIMP_EMAIL_LIST_ID     = "f3d2fd2988"

# ######## END MAILCHIMP settings ################



STRIPE_SECRET_KEY = "sk_test_51Gxu7mBgsgm0vdRS0V3qyVq8CmdM7ZW13BYNylWjlfyyAGKPLfpoZcQAKzePNZcqYgMn6aBeG0pVMfl7VWiPwX9X00yQRBPTah"
STRIPE_PUB_KEY = 'pk_test_51Gxu7mBgsgm0vdRSpZaF0ImDWNJH9ZW1d0lHyzo9KiHSPxkvktfStGLDMDvgtbKzuFAjitgFUoLvUhSGL122yE0Y00fSOJwl2M'

SITE_ID = 1



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'


ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'apps/products/templates'),
            os.path.join(BASE_DIR, 'apps/search/templates'),
            os.path.join(BASE_DIR, 'apps/carts/templates'),
            os.path.join(BASE_DIR, 'apps/accounts/templates'),
            os.path.join(BASE_DIR, 'apps/addresses/templates'),
            os.path.join(BASE_DIR, 'apps/billing/templates'),
            os.path.join(BASE_DIR, 'apps/marketing/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
# -*- coding: utf-8 -*-