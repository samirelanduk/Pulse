import os

DEBUG = True

if DEBUG:
    from .secrets import SECRET_KEY
    ALLOWED_HOSTS = []
else:
    SECRET_KEY = os.environ["SECRETKEY"]
    ALLOWED_HOSTS = ["*"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = "core.urls"

INSTALLED_APPS = [
 "django.contrib.staticfiles",
 "core",
]

TEMPLATES = [{
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "APP_DIRS": True,
}]

MIDDLEWARE = []

STATIC_URL = "/assets/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SASS_PROCESSOR_ROOT = os.path.abspath(f"{BASE_DIR}/core/static")
