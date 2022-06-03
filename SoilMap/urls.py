from django.contrib import admin
from django.urls import path, include
from SoilMap.views import CesiumActivityCreateView, CesiumActivityListView, CesiumActivityDetailView

urlpatterns = [
    path['cesiumactivity/create/', CesiumActivityCreateView.as_view()],
    path['cesiumactivity/all/', CesiumActivityListView.as_view()],
    path['cesiumactivity/detail/<uuid:pk>/', CesiumActivityDetailView.as_view()],
]
