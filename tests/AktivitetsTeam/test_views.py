import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_AktivitetsTeamItem_list_view(client):
    instance1 = test_helpers.create_AktivitetsTeam_AktivitetsTeamItem()
    instance2 = test_helpers.create_AktivitetsTeam_AktivitetsTeamItem()
    url = reverse("AktivitetsTeam_AktivitetsTeamItem_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_AktivitetsTeamItem_create_view(client):
    url = reverse("AktivitetsTeam_AktivitetsTeamItem_create")
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_AktivitetsTeamItem_detail_view(client):
    instance = test_helpers.create_AktivitetsTeam_AktivitetsTeamItem()
    url = reverse("AktivitetsTeam_AktivitetsTeamItem_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_AktivitetsTeamItem_update_view(client):
    instance = test_helpers.create_AktivitetsTeam_AktivitetsTeamItem()
    url = reverse("AktivitetsTeam_AktivitetsTeamItem_update", args=[instance.pk, ])
    data = {
        "description": "text",
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_AktivitetsTeamBooking_list_view(client):
    instance1 = test_helpers.create_AktivitetsTeam_AktivitetsTeamBooking()
    instance2 = test_helpers.create_AktivitetsTeam_AktivitetsTeamBooking()
    url = reverse("AktivitetsTeam_AktivitetsTeamBooking_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_AktivitetsTeamBooking_create_view(client):
    team = test_helpers.create_organization_Team()
    item = test_helpers.create_AktivitetsTeam_AktivitetsTeamItem()
    team_contact = test_helpers.create_organization_Volunteer()
    url = reverse("AktivitetsTeam_AktivitetsTeamBooking_create")
    data = {
        "location": "text",
        "start": datetime.now(),
        "end": datetime.now(),
        "remarks": "text",
        "status": "text",
        "team": team.pk,
        "item": item.pk,
        "team_contact": team_contact.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_AktivitetsTeamBooking_detail_view(client):
    instance = test_helpers.create_AktivitetsTeam_AktivitetsTeamBooking()
    url = reverse("AktivitetsTeam_AktivitetsTeamBooking_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_AktivitetsTeamBooking_update_view(client):
    team = test_helpers.create_organization_Team()
    item = test_helpers.create_AktivitetsTeam_AktivitetsTeamItem()
    team_contact = test_helpers.create_organization_Volunteer()
    instance = test_helpers.create_AktivitetsTeam_AktivitetsTeamBooking()
    url = reverse("AktivitetsTeam_AktivitetsTeamBooking_update", args=[instance.pk, ])
    data = {
        "location": "text",
        "start": datetime.now(),
        "end": datetime.now(),
        "remarks": "text",
        "status": "text",
        "team": team.pk,
        "item": item.pk,
        "team_contact": team_contact.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
