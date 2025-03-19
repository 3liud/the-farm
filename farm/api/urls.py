from django.urls import include, path
from rest_framework import routers

from .views import CountyViewSet, ItemCategoryViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r"counties", CountyViewSet)
router.register(r"categories", ItemCategoryViewSet)
router.register(r"items", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
