from rest_framework import viewsets

from .models import County, Item, ItemCategory
from .serializers import (CountySerializer, ItemCategorySerializer,
                          ItemSerializer)


class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer


class ItemCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.select_related("category").all()
    serializer_class = ItemSerializer
