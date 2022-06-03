from rest_framework import generics
from SoilMap.serializers import CesiumActivityDetailSerializer
from SoilMap.Models import CesiumActivity
from rest_framework.permissions import IsAuthenticated


class CesiumActivityCreateView(generics.CreateAPIView):
    serializer_class = CesiumActivityDetailSerializer
    permission_classes = IsAuthenticated


class CesiumActivityListView(generics.ListAPIView):
    serializer_class = CesiumActivityDetailSerializer
    queryset = CesiumActivity.objects.all()


class CesiumActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CesiumActivityDetailSerializer
    queryset = CesiumActivity.objects.all()
    permission_classes = IsAuthenticated
