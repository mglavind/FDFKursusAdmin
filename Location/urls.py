from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("LocationType", api.LocationTypeViewSet)
router.register("LocationBooking", api.LocationBookingViewSet)
router.register("LocationItem", api.LocationItemViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Location/LocationType/", views.LocationTypeListView.as_view(), name="Location_LocationType_list"),
    path("Location/LocationType/create/", views.LocationTypeCreateView.as_view(), name="Location_LocationType_create"),
    path("Location/LocationType/detail/<int:pk>/", views.LocationTypeDetailView.as_view(), name="Location_LocationType_detail"),
    path("Location/LocationType/update/<int:pk>/", views.LocationTypeUpdateView.as_view(), name="Location_LocationType_update"),
    path("Location/LocationType/delete/<int:pk>/", views.LocationTypeDeleteView.as_view(), name="Location_LocationType_delete"),
    path("Location/LocationBooking/", views.LocationBookingListView.as_view(), name="Location_LocationBooking_list"),
    path("Location/LocationBooking/create/", views.LocationBookingCreateView.as_view(), name="Location_LocationBooking_create"),
    path("Location/LocationBooking/detail/<int:pk>/", views.LocationBookingDetailView.as_view(), name="Location_LocationBooking_detail"),
    path("Location/LocationBooking/update/<int:pk>/", views.LocationBookingUpdateView.as_view(), name="Location_LocationBooking_update"),
    path("Location/LocationBooking/delete/<int:pk>/", views.LocationBookingDeleteView.as_view(), name="Location_LocationBooking_delete"),
    path("Location/LocationItem/", views.LocationItemListView.as_view(), name="Location_LocationItem_list"),
    path("Location/LocationItem/create/", views.LocationItemCreateView.as_view(), name="Location_LocationItem_create"),
    path("Location/LocationItem/detail/<int:pk>/", views.LocationItemDetailView.as_view(), name="Location_LocationItem_detail"),
    path("Location/LocationItem/update/<int:pk>/", views.LocationItemUpdateView.as_view(), name="Location_LocationItem_update"),
    path("Location/LocationItem/delete/<int:pk>/", views.LocationItemDeleteView.as_view(), name="Location_LocationItem_delete"),

)
