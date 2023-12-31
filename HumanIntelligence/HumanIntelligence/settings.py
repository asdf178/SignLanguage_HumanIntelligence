import os

"""
Django settings for HumanIntelligence project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wn$f&1m^!@zdv442+-ens_-6&d2q35)@dejw7m6go1dz9k$kho"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "main.apps.MainConfig",
    "register.apps.RegisterConfig",
    "exam.apps.ExamConfig",
    "learn.apps.LearnConfig",
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

ROOT_URLCONF = "HumanIntelligence.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "HumanIntelligence.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/images/"
MEDIA_ROOT = os.path.join(BASE_DIR, "images")

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = "/home"
LOGOUT_REDIRECT_URL = "/home"

IMAGE_LIST = {
    name[:-4]: "../../../static/images/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "images/"))
}
VIDEO_LIST = {
    name[:-4]: "../../../static/videos/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "videos/"))
}
ima_ga_LIST = {
    name[:-4]: "../../../static/ima_ga/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_ga/"))
}
ima_na_LIST = {
    name[:-4]: "../../../static/ima_na/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_na/"))
}
ima_da_LIST = {
    name[:-4]: "../../../static/ima_da/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_da/"))
}
ima_ba_LIST = {
    name[:-4]: "../../../static/ima_ba/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_ba/"))
}
ima_sa_LIST = {
    name[:-4]: "../../../static/ima_sa/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_sa/"))
}
ima_ah_LIST = {
    name[:-4]: "../../../static/ima_ah/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_ah/"))
}
ima_ja_LIST = {
    name[:-4]: "../../../static/ima_ja/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_ja/"))
}
ima_cha_LIST = {
    name[:-4]: "../../../static/ima_cha/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_cha/"))
}
ima_ha_LIST = {
    name[:-4]: "../../../static/ima_ha/" + name
    for name in os.listdir(os.path.join(STATICFILES_DIRS[0], "ima_ha/"))
}