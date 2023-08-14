import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_SjakItem_list_view(client):
    instance1 = test_helpers.create_Sjak_SjakItem()
    instance2 = test_helpers.create_Sjak_SjakItem()
    url = reverse("Sjak_SjakItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SjakItem_create_view(client):
    type = test_helpers.create_Sjak_SjakItemType()
    url = reverse("Sjak_SjakItem_create")
    data = {
        "name": "text",
        "description": "text",
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SjakItem_detail_view(client):
    instance = test_helpers.create_Sjak_SjakItem()
    url = reverse("Sjak_SjakItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SjakItem_update_view(client):
    type = test_helpers.create_Sjak_SjakItemType()
    instance = test_helpers.create_Sjak_SjakItem()
    url = reverse("Sjak_SjakItem_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "description": "text",
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SjakBooking_list_view(client):
    instance1 = test_helpers.create_Sjak_SjakBooking()
    instance2 = test_helpers.create_Sjak_SjakBooking()
    url = reverse("Sjak_SjakBooking_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SjakBooking_create_view(client):
    item = test_helpers.create_Sjak_SjakItem()
    team_contact = test_helpers.create_organization_Volunteer()
    team = test_helpers.create_organization_Team()
    url = reverse("Sjak_SjakBooking_create")
    data = {
        "remarks": "text",
        "status": "text",
        "quantity": 1.0,
        "use_date": datetime.now(),
        "item": item.pk,
        "team_contact": team_contact.pk,
        "team": team.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SjakBooking_detail_view(client):
    instance = test_helpers.create_Sjak_SjakBooking()
    url = reverse("Sjak_SjakBooking_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SjakBooking_update_view(client):
    item = test_helpers.create_Sjak_SjakItem()
    team_contact = test_helpers.create_organization_Volunteer()
    team = test_helpers.create_organization_Team()
    instance = test_helpers.create_Sjak_SjakBooking()
    url = reverse("Sjak_SjakBooking_update", args=[instance.pk, ])
    data = {
        "remarks": "text",
        "status": "text",
        "quantity": 1.0,
        "use_date": datetime.now(),
        "item": item.pk,
        "team_contact": team_contact.pk,
        "team": team.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SjakItemType_list_view(client):
    instance1 = test_helpers.create_Sjak_SjakItemType()
    instance2 = test_helpers.create_Sjak_SjakItemType()
    url = reverse("Sjak_SjakItemType_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SjakItemType_create_view(client):
    url = reverse("Sjak_SjakItemType_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SjakItemType_detail_view(client):
    instance = test_helpers.create_Sjak_SjakItemType()
    url = reverse("Sjak_SjakItemType_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SjakItemType_update_view(client):
    instance = test_helpers.create_Sjak_SjakItemType()
    url = reverse("Sjak_SjakItemType_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
