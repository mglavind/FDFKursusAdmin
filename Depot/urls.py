from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("DepotItem", api.DepotItemViewSet)
router.register("DepotLocation", api.DepotLocationViewSet)
router.register("DepotBooking", api.DepotBookingViewSet)
router.register("DepotBox", api.DepotBoxViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Depot/DepotItem/", views.DepotItemListView.as_view(), name="Depot_DepotItem_list"),
    path("Depot/DepotItem/create/", views.DepotItemCreateView.as_view(), name="Depot_DepotItem_create"),
    path("Depot/DepotItem/detail/<int:pk>/", views.DepotItemDetailView.as_view(), name="Depot_DepotItem_detail"),
    path("Depot/DepotItem/update/<int:pk>/", views.DepotItemUpdateView.as_view(), name="Depot_DepotItem_update"),
    path("Depot/DepotItem/delete/<int:pk>/", views.DepotItemDeleteView.as_view(), name="Depot_DepotItem_delete"),
    path("Depot/DepotLocation/", views.DepotLocationListView.as_view(), name="Depot_DepotLocation_list"),
    path("Depot/DepotLocation/create/", views.DepotLocationCreateView.as_view(), name="Depot_DepotLocation_create"),
    path("Depot/DepotLocation/detail/<int:pk>/", views.DepotLocationDetailView.as_view(), name="Depot_DepotLocation_detail"),
    path("Depot/DepotLocation/update/<int:pk>/", views.DepotLocationUpdateView.as_view(), name="Depot_DepotLocation_update"),
    path("Depot/DepotLocation/delete/<int:pk>/", views.DepotLocationDeleteView.as_view(), name="Depot_DepotLocation_delete"),
    path("Depot/DepotBooking/", views.DepotBookingListView.as_view(), name="Depot_DepotBooking_list"),
    path("Depot/DepotBooking/create/", views.DepotBookingCreateView.as_view(), name="Depot_DepotBooking_create"),
    path("Depot/DepotBooking/detail/<int:pk>/", views.DepotBookingDetailView.as_view(), name="Depot_DepotBooking_detail"),
    path("Depot/DepotBooking/update/<int:pk>/", views.DepotBookingUpdateView.as_view(), name="Depot_DepotBooking_update"),
    path("Depot/DepotBooking/delete/<int:pk>/", views.DepotBookingDeleteView.as_view(), name="Depot_DepotBooking_delete"),
    path("Depot/DepotBox/", views.DepotBoxListView.as_view(), name="Depot_DepotBox_list"),
    path("Depot/DepotBox/create/", views.DepotBoxCreateView.as_view(), name="Depot_DepotBox_create"),
    path("Depot/DepotBox/detail/<int:pk>/", views.DepotBoxDetailView.as_view(), name="Depot_DepotBox_detail"),
    path("Depot/DepotBox/update/<int:pk>/", views.DepotBoxUpdateView.as_view(), name="Depot_DepotBox_update"),
    path("Depot/DepotBox/delete/<int:pk>/", views.DepotBoxDeleteView.as_view(), name="Depot_DepotBox_delete"),

)
