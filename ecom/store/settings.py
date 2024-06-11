import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from django.contrib import admin
from django.urls import path, include

#Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

#Quick start development settings--UNSUITABLE FOR PRODUCTION

#SECURITY WARNING: KEEP THE SECRET KEY IN A SECRET FILE
# Add .env variables anywhere before SECRET_KEY
load_dotenv(find_dotenv())

# UPDATE secret key
SECRET_KEY = os.environ['SECRET_KEY'] # Instead of your actual secret key

#SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS= []

#Application definition

INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",  
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  "store",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecommerce_website.urls"

WSGI_APPLICATION = "ecommerce_website.wsgi.application"

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django_template.context-processors.debug",
        "django_template.context-processors.request",
        "django.contribute.auth.context_processors.auth",
        "django.contribute.messages.context_processors.messages",
      ]
    }
  }
]

#Database
#https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
  }
}

#Password validation
#https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password

AUTH_PASSWORD_VALIDATORS = [
  {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
  }
]

#Internatinalization
#https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#Static files (CSS, JavaScript, Images)
#https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = ["static"]

#Allow us to upload pictures
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

