import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_TeknikItem_list_view(client):
    instance1 = test_helpers.create_Teknik_TeknikItem()
    instance2 = test_helpers.create_Teknik_TeknikItem()
    url = reverse("Teknik_TeknikItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TeknikItem_create_view(client):
    url = reverse("Teknik_TeknikItem_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TeknikItem_detail_view(client):
    instance = test_helpers.create_Teknik_TeknikItem()
    url = reverse("Teknik_TeknikItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TeknikItem_update_view(client):
    instance = test_helpers.create_Teknik_TeknikItem()
    url = reverse("Teknik_TeknikItem_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TeknikBooking_list_view(client):
    instance1 = test_helpers.create_Teknik_TeknikBooking()
    instance2 = test_helpers.create_Teknik_TeknikBooking()
    url = reverse("Teknik_TeknikBooking_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TeknikBooking_create_view(client):
    url = reverse("Teknik_TeknikBooking_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TeknikBooking_detail_view(client):
    instance = test_helpers.create_Teknik_TeknikBooking()
    url = reverse("Teknik_TeknikBooking_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TeknikBooking_update_view(client):
    instance = test_helpers.create_Teknik_TeknikBooking()
    url = reverse("Teknik_TeknikBooking_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
