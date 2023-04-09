from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("MadItem", api.MadItemViewSet)
router.register("MadKategori", api.MadKategoriViewSet)
router.register("MadBooking", api.MadBookingViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Mad/MadItem/", views.MadItemListView.as_view(), name="Mad_MadItem_list"),
    path("Mad/MadItem/create/", views.MadItemCreateView.as_view(), name="Mad_MadItem_create"),
    path("Mad/MadItem/detail/<int:pk>/", views.MadItemDetailView.as_view(), name="Mad_MadItem_detail"),
    path("Mad/MadItem/update/<int:pk>/", views.MadItemUpdateView.as_view(), name="Mad_MadItem_update"),
    path("Mad/MadItem/delete/<int:pk>/", views.MadItemDeleteView.as_view(), name="Mad_MadItem_delete"),
    path("Mad/MadKategori/", views.MadKategoriListView.as_view(), name="Mad_MadKategori_list"),
    path("Mad/MadKategori/create/", views.MadKategoriCreateView.as_view(), name="Mad_MadKategori_create"),
    path("Mad/MadKategori/detail/<int:pk>/", views.MadKategoriDetailView.as_view(), name="Mad_MadKategori_detail"),
    path("Mad/MadKategori/update/<int:pk>/", views.MadKategoriUpdateView.as_view(), name="Mad_MadKategori_update"),
    path("Mad/MadKategori/delete/<int:pk>/", views.MadKategoriDeleteView.as_view(), name="Mad_MadKategori_delete"),
    path("Mad/MadBooking/", views.MadBookingListView.as_view(), name="Mad_MadBooking_list"),
    path("Mad/MadBooking/create/", views.MadBookingCreateView.as_view(), name="Mad_MadBooking_create"),
    path("Mad/MadBooking/detail/<int:pk>/", views.MadBookingDetailView.as_view(), name="Mad_MadBooking_detail"),
    path("Mad/MadBooking/update/<int:pk>/", views.MadBookingUpdateView.as_view(), name="Mad_MadBooking_update"),
    path("Mad/MadBooking/delete/<int:pk>/", views.MadBookingDeleteView.as_view(), name="Mad_MadBooking_delete"),

)
