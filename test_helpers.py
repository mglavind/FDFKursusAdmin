import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from KursusOrganisation import models as KursusOrganisation_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_KursusOrganisation_Medarbejder(**kwargs):
    defaults = {}
    defaults["last_updated"] = datetime.now()
    defaults["navn"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_User()
    defaults.update(**kwargs)
    return KursusOrganisation_models.Medarbejder.objects.create(**defaults)
def create_KursusOrganisation_Kursus(**kwargs):
    defaults = {}
    defaults["start_date"] = datetime.now()
    defaults["last_updated"] = datetime.now()
    defaults["navn"] = ""
    defaults["end_date"] = datetime.now()
    defaults.update(**kwargs)
    return KursusOrganisation_models.Kursus.objects.create(**defaults)
def create_KursusOrganisation_Team(**kwargs):
    defaults = {}
    defaults["last_updated"] = datetime.now()
    defaults["navn"] = ""
    if "medarbejder" not in kwargs:
        defaults["medarbejder"] = create_KursusOrganisation_Medarbejder()
    if "kursus" not in kwargs:
        defaults["kursus"] = create_KursusOrganisation_Kursus()
    defaults.update(**kwargs)
    return KursusOrganisation_models.Team.objects.create(**defaults)
