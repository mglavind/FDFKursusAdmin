from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("FotoItem", api.FotoItemViewSet)
router.register("FotoBooking", api.FotoBookingViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Foto/FotoItem/", views.FotoItemListView.as_view(), name="Foto_FotoItem_list"),
    path("Foto/FotoItem/create/", views.FotoItemCreateView.as_view(), name="Foto_FotoItem_create"),
    path("Foto/FotoItem/detail/<int:pk>/", views.FotoItemDetailView.as_view(), name="Foto_FotoItem_detail"),
    path("Foto/FotoItem/update/<int:pk>/", views.FotoItemUpdateView.as_view(), name="Foto_FotoItem_update"),
    path("Foto/FotoItem/delete/<int:pk>/", views.FotoItemDeleteView.as_view(), name="Foto_FotoItem_delete"),
    path("Foto/FotoBooking/", views.FotoBookingListView.as_view(), name="Foto_FotoBooking_list"),
    path("Foto/FotoBooking/create/", views.FotoBookingCreateView.as_view(), name="Foto_FotoBooking_create"),
    path("Foto/FotoBooking/detail/<int:pk>/", views.FotoBookingDetailView.as_view(), name="Foto_FotoBooking_detail"),
    path("Foto/FotoBooking/update/<int:pk>/", views.FotoBookingUpdateView.as_view(), name="Foto_FotoBooking_update"),
    path("Foto/FotoBooking/delete/<int:pk>/", views.FotoBookingDeleteView.as_view(), name="Foto_FotoBooking_delete"),

)
