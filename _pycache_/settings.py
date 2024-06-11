#Django settings for ecommerce project.
#Gnerated by "django-admin startproject" using Django 2.2.6.

from pathlib import __path__
from re import TEMPLATE
import os

#Buit path inside the object BASE_DIR / "subfolder"
BASE_DIR = Path(__file__).resolve().parent.parent

#Quick-start development settings - unsuitable for production

#See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

#SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = "django-insecure-p@$$w0rd"

#SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

#Application definition
INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",  

  #Custom apps
  "core", 
  #Might also have apps like "blog", "store"
]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.message.middlware.MessageMiddleware",
  "djangos.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
  "BACKEND": "django.template.backends.django.DjangoTemplates",
  "DIRS": [os.path.join(BASE_DIR, "templates")],
  "APP_DIRS": True,
]