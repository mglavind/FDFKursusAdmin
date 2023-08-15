import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_ButikkenItem_list_view(client):
    instance1 = test_helpers.create_Butikken_ButikkenItem()
    instance2 = test_helpers.create_Butikken_ButikkenItem()
    url = reverse("Butikken_ButikkenItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ButikkenItem_create_view(client):
    type = test_helpers.create_Butikken_ButikkenItemType()
    url = reverse("Butikken_ButikkenItem_create")
    data = {
        "description": "text",
        "name": "text",
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ButikkenItem_detail_view(client):
    instance = test_helpers.create_Butikken_ButikkenItem()
    url = reverse("Butikken_ButikkenItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ButikkenItem_update_view(client):
    type = test_helpers.create_Butikken_ButikkenItemType()
    instance = test_helpers.create_Butikken_ButikkenItem()
    url = reverse("Butikken_ButikkenItem_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
        "type": type.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ButikkenBooking_list_view(client):
    instance1 = test_helpers.create_Butikken_ButikkenBooking()
    instance2 = test_helpers.create_Butikken_ButikkenBooking()
    url = reverse("Butikken_ButikkenBooking_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ButikkenBooking_create_view(client):
    team = test_helpers.create_organization_Team()
    item = test_helpers.create_Butikken_ButikkenItem()
    team_contact = test_helpers.create_organization_Volunteer()
    url = reverse("Butikken_ButikkenBooking_create")
    data = {
        "remarks": "text",
        "quantity": 1.0,
        "status": "text",
        "start": datetime.now(),
        "team": team.pk,
        "item": item.pk,
        "team_contact": team_contact.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ButikkenBooking_detail_view(client):
    instance = test_helpers.create_Butikken_ButikkenBooking()
    url = reverse("Butikken_ButikkenBooking_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ButikkenBooking_update_view(client):
    team = test_helpers.create_organization_Team()
    item = test_helpers.create_Butikken_ButikkenItem()
    team_contact = test_helpers.create_organization_Volunteer()
    instance = test_helpers.create_Butikken_ButikkenBooking()
    url = reverse("Butikken_ButikkenBooking_update", args=[instance.pk, ])
    data = {
        "remarks": "text",
        "quantity": 1.0,
        "status": "text",
        "start": datetime.now(),
        "team": team.pk,
        "item": item.pk,
        "team_contact": team_contact.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ButikkenItemType_list_view(client):
    instance1 = test_helpers.create_Butikken_ButikkenItemType()
    instance2 = test_helpers.create_Butikken_ButikkenItemType()
    url = reverse("Butikken_ButikkenItemType_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ButikkenItemType_create_view(client):
    url = reverse("Butikken_ButikkenItemType_create")
    data = {
        "name": "text",
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ButikkenItemType_detail_view(client):
    instance = test_helpers.create_Butikken_ButikkenItemType()
    url = reverse("Butikken_ButikkenItemType_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ButikkenItemType_update_view(client):
    instance = test_helpers.create_Butikken_ButikkenItemType()
    url = reverse("Butikken_ButikkenItemType_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
