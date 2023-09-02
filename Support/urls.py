from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("SupportItem", api.SupportItemViewSet)
router.register("SupportBooking", api.SupportBookingViewSet)
router.register("SupportItemType", api.SupportItemTypeViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Support/SupportItem/", views.SupportItemListView.as_view(), name="Support_SupportItem_list"),
    path("Support/SupportItem/create/", views.SupportItemCreateView.as_view(), name="Support_SupportItem_create"),
    path("Support/SupportItem/detail/<int:pk>/", views.SupportItemDetailView.as_view(), name="Support_SupportItem_detail"),
    path("Support/SupportItem/update/<int:pk>/", views.SupportItemUpdateView.as_view(), name="Support_SupportItem_update"),
    path("Support/SupportItem/delete/<int:pk>/", views.SupportItemDeleteView.as_view(), name="Support_SupportItem_delete"),
    path("Support/SupportBooking/", views.SupportBookingListView.as_view(), name="Support_SupportBooking_list"),
    path("Support/SupportBooking/create/", views.SupportBookingCreateView.as_view(), name="Support_SupportBooking_create"),
    path("Support/SupportBooking/detail/<int:pk>/", views.SupportBookingDetailView.as_view(), name="Support_SupportBooking_detail"),
    path("Support/SupportBooking/update/<int:pk>/", views.SupportBookingUpdateView.as_view(), name="Support_SupportBooking_update"),
    path("Support/SupportBooking/delete/<int:pk>/", views.SupportBookingDeleteView.as_view(), name="Support_SupportBooking_delete"),
    path("Support/SupportItemType/", views.SupportItemTypeListView.as_view(), name="Support_SupportItemType_list"),
    path("Support/SupportItemType/create/", views.SupportItemTypeCreateView.as_view(), name="Support_SupportItemType_create"),
    path("Support/SupportItemType/detail/<int:pk>/", views.SupportItemTypeDetailView.as_view(), name="Support_SupportItemType_detail"),
    path("Support/SupportItemType/update/<int:pk>/", views.SupportItemTypeUpdateView.as_view(), name="Support_SupportItemType_update"),
    path("Support/SupportItemType/delete/<int:pk>/", views.SupportItemTypeDeleteView.as_view(), name="Support_SupportItemType_delete"),

)
