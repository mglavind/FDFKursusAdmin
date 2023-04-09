from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Medarbejder", api.MedarbejderViewSet)
router.register("Kursus", api.KursusViewSet)
router.register("Team", api.TeamViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("KursusOrganisation/Medarbejder/", views.MedarbejderListView.as_view(), name="KursusOrganisation_Medarbejder_list"),
    path("KursusOrganisation/Medarbejder/create/", views.MedarbejderCreateView.as_view(), name="KursusOrganisation_Medarbejder_create"),
    path("KursusOrganisation/Medarbejder/detail/<int:pk>/", views.MedarbejderDetailView.as_view(), name="KursusOrganisation_Medarbejder_detail"),
    path("KursusOrganisation/Medarbejder/update/<int:pk>/", views.MedarbejderUpdateView.as_view(), name="KursusOrganisation_Medarbejder_update"),
    path("KursusOrganisation/Medarbejder/delete/<int:pk>/", views.MedarbejderDeleteView.as_view(), name="KursusOrganisation_Medarbejder_delete"),
    path("KursusOrganisation/Kursus/", views.KursusListView.as_view(), name="KursusOrganisation_Kursus_list"),
    path("KursusOrganisation/Kursus/create/", views.KursusCreateView.as_view(), name="KursusOrganisation_Kursus_create"),
    path("KursusOrganisation/Kursus/detail/<int:pk>/", views.KursusDetailView.as_view(), name="KursusOrganisation_Kursus_detail"),
    path("KursusOrganisation/Kursus/update/<int:pk>/", views.KursusUpdateView.as_view(), name="KursusOrganisation_Kursus_update"),
    path("KursusOrganisation/Kursus/delete/<int:pk>/", views.KursusDeleteView.as_view(), name="KursusOrganisation_Kursus_delete"),
    path("KursusOrganisation/Team/", views.TeamListView.as_view(), name="KursusOrganisation_Team_list"),
    path("KursusOrganisation/Team/create/", views.TeamCreateView.as_view(), name="KursusOrganisation_Team_create"),
    path("KursusOrganisation/Team/detail/<int:pk>/", views.TeamDetailView.as_view(), name="KursusOrganisation_Team_detail"),
    path("KursusOrganisation/Team/update/<int:pk>/", views.TeamUpdateView.as_view(), name="KursusOrganisation_Team_update"),
    path("KursusOrganisation/Team/delete/<int:pk>/", views.TeamDeleteView.as_view(), name="KursusOrganisation_Team_delete"),

)
