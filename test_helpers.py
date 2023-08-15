import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from organization import models as organization_models
from Teknik import models as Teknik_models
from Sjak import models as Sjak_models
from AktivitetsTeam import models as AktivitetsTeam_models

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


def create_organization_TeamMembership(**kwargs):
    defaults = {}
    defaults["role"] = ""
    if "team" not in kwargs:
        defaults["team"] = create_Organization_Team()
    if "member" not in kwargs:
        defaults["member"] = create_Organization_Volunteer()
    defaults.update(**kwargs)
    return organization_models.TeamMembership.objects.create(**defaults)
def create_organization_EventMembership(**kwargs):
    defaults = {}
    if "member" not in kwargs:
        defaults["member"] = create_Organization_Volunteer()
    if "event" not in kwargs:
        defaults["event"] = create_Organization_Event()
    defaults.update(**kwargs)
    return organization_models.EventMembership.objects.create(**defaults)
def create_organization_Event(**kwargs):
    defaults = {}
    defaults["start_date"] = datetime.now()
    defaults["end_date"] = datetime.now()
    defaults["name"] = ""
    defaults.update(**kwargs)
    return organization_models.Event.objects.create(**defaults)
def create_organization_Team(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["short_name"] = ""
    defaults.update(**kwargs)
    return organization_models.Team.objects.create(**defaults)
def create_organization_Volunteer(**kwargs):
    defaults = {}
    defaults["email"] = ""
    defaults["phone"] = ""
    defaults["first_name"] = ""
    defaults["first_name"] = ""
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return organization_models.Volunteer.objects.create(**defaults)
def create_Teknik_TeknikType(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return Teknik_models.TeknikType.objects.create(**defaults)
def create_Teknik_TeknikBooking(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults["start"] = datetime.now()
    defaults["quantity"] = ""
    defaults["end"] = datetime.now()
    if "team" not in kwargs:
        defaults["team"] = create_organization_Team()
    if "item" not in kwargs:
        defaults["item"] = create_Teknik_TeknikItem()
    if "team_contact" not in kwargs:
        defaults["team_contact"] = create_organization_Volunteer()
    defaults.update(**kwargs)
    return Teknik_models.TeknikBooking.objects.create(**defaults)
def create_Teknik_TeknikItem(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["name"] = ""
    defaults["image"] = ""
    if "owner" not in kwargs:
        defaults["owner"] = create_Group()
    if "type" not in kwargs:
        defaults["type"] = create_Teknik_TeknikType()
    defaults.update(**kwargs)
    return Teknik_models.TeknikItem.objects.create(**defaults)
def create_Sjak_SjakItem(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["description"] = ""
    if "type" not in kwargs:
        defaults["type"] = create_Sjak_SjakItemType()
    defaults.update(**kwargs)
    return Sjak_models.SjakItem.objects.create(**defaults)
def create_Sjak_SjakBooking(**kwargs):
    defaults = {}
    defaults["remarks"] = ""
    defaults["status"] = ""
    defaults["quantity"] = ""
    defaults["use_date"] = datetime.now()
    if "item" not in kwargs:
        defaults["item"] = create_Sjak_SjakItem()
    if "team_contact" not in kwargs:
        defaults["team_contact"] = create_organization_Volunteer()
    if "team" not in kwargs:
        defaults["team"] = create_organization_Team()
    defaults.update(**kwargs)
    return Sjak_models.SjakBooking.objects.create(**defaults)
def create_Sjak_SjakItemType(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return Sjak_models.SjakItemType.objects.create(**defaults)
def create_AktivitetsTeam_AktivitetsTeamItem(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["name"] = ""
    defaults.update(**kwargs)
    return AktivitetsTeam_models.AktivitetsTeamItem.objects.create(**defaults)
def create_AktivitetsTeam_AktivitetsTeamBooking(**kwargs):
    defaults = {}
    defaults["location"] = ""
    defaults["start"] = datetime.now()
    defaults["end"] = datetime.now()
    defaults["remarks"] = ""
    defaults["status"] = ""
    if "team" not in kwargs:
        defaults["team"] = create_organization_Team()
    if "item" not in kwargs:
        defaults["item"] = create_AktivitetsTeam_AktivitetsTeamItem()
    if "team_contact" not in kwargs:
        defaults["team_contact"] = create_organization_Volunteer()
    defaults.update(**kwargs)
    return AktivitetsTeam_models.AktivitetsTeamBooking.objects.create(**defaults)
