import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Medarbejder_list_view(client):
    instance1 = test_helpers.create_KursusOrganisation_Medarbejder()
    instance2 = test_helpers.create_KursusOrganisation_Medarbejder()
    url = reverse("KursusOrganisation_Medarbejder_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Medarbejder_create_view(client):
    user = test_helpers.create_User()
    url = reverse("KursusOrganisation_Medarbejder_create")
    data = {
        "last_updated": datetime.now(),
        "navn": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Medarbejder_detail_view(client):
    instance = test_helpers.create_KursusOrganisation_Medarbejder()
    url = reverse("KursusOrganisation_Medarbejder_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Medarbejder_update_view(client):
    user = test_helpers.create_User()
    instance = test_helpers.create_KursusOrganisation_Medarbejder()
    url = reverse("KursusOrganisation_Medarbejder_update", args=[instance.pk, ])
    data = {
        "last_updated": datetime.now(),
        "navn": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Kursus_list_view(client):
    instance1 = test_helpers.create_KursusOrganisation_Kursus()
    instance2 = test_helpers.create_KursusOrganisation_Kursus()
    url = reverse("KursusOrganisation_Kursus_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Kursus_create_view(client):
    url = reverse("KursusOrganisation_Kursus_create")
    data = {
        "start_date": datetime.now(),
        "last_updated": datetime.now(),
        "navn": "text",
        "end_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Kursus_detail_view(client):
    instance = test_helpers.create_KursusOrganisation_Kursus()
    url = reverse("KursusOrganisation_Kursus_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Kursus_update_view(client):
    instance = test_helpers.create_KursusOrganisation_Kursus()
    url = reverse("KursusOrganisation_Kursus_update", args=[instance.pk, ])
    data = {
        "start_date": datetime.now(),
        "last_updated": datetime.now(),
        "navn": "text",
        "end_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Team_list_view(client):
    instance1 = test_helpers.create_KursusOrganisation_Team()
    instance2 = test_helpers.create_KursusOrganisation_Team()
    url = reverse("KursusOrganisation_Team_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Team_create_view(client):
    medarbejder = test_helpers.create_KursusOrganisation_Medarbejder()
    kursus = test_helpers.create_KursusOrganisation_Kursus()
    url = reverse("KursusOrganisation_Team_create")
    data = {
        "last_updated": datetime.now(),
        "navn": "text",
        "medarbejder": medarbejder.pk,
        "kursus": kursus.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Team_detail_view(client):
    instance = test_helpers.create_KursusOrganisation_Team()
    url = reverse("KursusOrganisation_Team_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Team_update_view(client):
    medarbejder = test_helpers.create_KursusOrganisation_Medarbejder()
    kursus = test_helpers.create_KursusOrganisation_Kursus()
    instance = test_helpers.create_KursusOrganisation_Team()
    url = reverse("KursusOrganisation_Team_update", args=[instance.pk, ])
    data = {
        "last_updated": datetime.now(),
        "navn": "text",
        "medarbejder": medarbejder.pk,
        "kursus": kursus.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
