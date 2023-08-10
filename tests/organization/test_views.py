import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Team_list_view(client):
    instance1 = test_helpers.create_organization_Team()
    instance2 = test_helpers.create_organization_Team()
    url = reverse("organization_Team_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Team_create_view(client):
    url = reverse("organization_Team_create")
    data = {
        "name": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Team_detail_view(client):
    instance = test_helpers.create_organization_Team()
    url = reverse("organization_Team_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Team_update_view(client):
    instance = test_helpers.create_organization_Team()
    url = reverse("organization_Team_update", args=[instance.slug, ])
    data = {
        "name": "text",
        "slug": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TeamMembership_list_view(client):
    instance1 = test_helpers.create_organization_TeamMembership()
    instance2 = test_helpers.create_organization_TeamMembership()
    url = reverse("organization_TeamMembership_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TeamMembership_create_view(client):
    team = test_helpers.create_Organization_Team()
    member = test_helpers.create_Organization_Volunteer()
    url = reverse("organization_TeamMembership_create")
    data = {
        "role": "text",
        "team": team.pk,
        "member": member.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TeamMembership_detail_view(client):
    instance = test_helpers.create_organization_TeamMembership()
    url = reverse("organization_TeamMembership_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TeamMembership_update_view(client):
    team = test_helpers.create_Organization_Team()
    member = test_helpers.create_Organization_Volunteer()
    instance = test_helpers.create_organization_TeamMembership()
    url = reverse("organization_TeamMembership_update", args=[instance.pk, ])
    data = {
        "role": "text",
        "team": team.pk,
        "member": member.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Event_list_view(client):
    instance1 = test_helpers.create_organization_Event()
    instance2 = test_helpers.create_organization_Event()
    url = reverse("organization_Event_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Event_create_view(client):
    url = reverse("organization_Event_create")
    data = {
        "end_date": datetime.now(),
        "name": "text",
        "start_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Event_detail_view(client):
    instance = test_helpers.create_organization_Event()
    url = reverse("organization_Event_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Event_update_view(client):
    instance = test_helpers.create_organization_Event()
    url = reverse("organization_Event_update", args=[instance.pk, ])
    data = {
        "end_date": datetime.now(),
        "name": "text",
        "start_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_EventMembership_list_view(client):
    instance1 = test_helpers.create_organization_EventMembership()
    instance2 = test_helpers.create_organization_EventMembership()
    url = reverse("organization_EventMembership_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_EventMembership_create_view(client):
    event = test_helpers.create_Organization_Event()
    member = test_helpers.create_Organization_Volunteer()
    url = reverse("organization_EventMembership_create")
    data = {
        "event": event.pk,
        "member": member.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_EventMembership_detail_view(client):
    instance = test_helpers.create_organization_EventMembership()
    url = reverse("organization_EventMembership_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_EventMembership_update_view(client):
    event = test_helpers.create_Organization_Event()
    member = test_helpers.create_Organization_Volunteer()
    instance = test_helpers.create_organization_EventMembership()
    url = reverse("organization_EventMembership_update", args=[instance.pk, ])
    data = {
        "event": event.pk,
        "member": member.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Volunteer_list_view(client):
    instance1 = test_helpers.create_organization_Volunteer()
    instance2 = test_helpers.create_organization_Volunteer()
    url = reverse("organization_Volunteer_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Volunteer_create_view(client):
    url = reverse("organization_Volunteer_create")
    data = {
        "first_name": "text",
        "first_name": "text",
        "email": "user@tempurl.com",
        "phone": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Volunteer_detail_view(client):
    instance = test_helpers.create_organization_Volunteer()
    url = reverse("organization_Volunteer_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Volunteer_update_view(client):
    instance = test_helpers.create_organization_Volunteer()
    url = reverse("organization_Volunteer_update", args=[instance.pk, ])
    data = {
        "first_name": "text",
        "first_name": "text",
        "email": "user@tempurl.com",
        "phone": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
