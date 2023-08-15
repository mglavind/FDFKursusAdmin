from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("ButikkenItem", api.ButikkenItemViewSet)
router.register("ButikkenBooking", api.ButikkenBookingViewSet)
router.register("ButikkenItemType", api.ButikkenItemTypeViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Butikken/ButikkenItem/", views.ButikkenItemListView.as_view(), name="Butikken_ButikkenItem_list"),
    path("Butikken/ButikkenItem/create/", views.ButikkenItemCreateView.as_view(), name="Butikken_ButikkenItem_create"),
    path("Butikken/ButikkenItem/detail/<int:pk>/", views.ButikkenItemDetailView.as_view(), name="Butikken_ButikkenItem_detail"),
    path("Butikken/ButikkenItem/update/<int:pk>/", views.ButikkenItemUpdateView.as_view(), name="Butikken_ButikkenItem_update"),
    path("Butikken/ButikkenItem/delete/<int:pk>/", views.ButikkenItemDeleteView.as_view(), name="Butikken_ButikkenItem_delete"),
    path("Butikken/ButikkenBooking/", views.ButikkenBookingListView.as_view(), name="Butikken_ButikkenBooking_list"),
    path("Butikken/ButikkenBooking/create/", views.ButikkenBookingCreateView.as_view(), name="Butikken_ButikkenBooking_create"),
    path("Butikken/ButikkenBooking/detail/<int:pk>/", views.ButikkenBookingDetailView.as_view(), name="Butikken_ButikkenBooking_detail"),
    path("Butikken/ButikkenBooking/update/<int:pk>/", views.ButikkenBookingUpdateView.as_view(), name="Butikken_ButikkenBooking_update"),
    path("Butikken/ButikkenBooking/delete/<int:pk>/", views.ButikkenBookingDeleteView.as_view(), name="Butikken_ButikkenBooking_delete"),
    path("Butikken/ButikkenItemType/", views.ButikkenItemTypeListView.as_view(), name="Butikken_ButikkenItemType_list"),
    path("Butikken/ButikkenItemType/create/", views.ButikkenItemTypeCreateView.as_view(), name="Butikken_ButikkenItemType_create"),
    path("Butikken/ButikkenItemType/detail/<int:pk>/", views.ButikkenItemTypeDetailView.as_view(), name="Butikken_ButikkenItemType_detail"),
    path("Butikken/ButikkenItemType/update/<int:pk>/", views.ButikkenItemTypeUpdateView.as_view(), name="Butikken_ButikkenItemType_update"),
    path("Butikken/ButikkenItemType/delete/<int:pk>/", views.ButikkenItemTypeDeleteView.as_view(), name="Butikken_ButikkenItemType_delete"),

)
