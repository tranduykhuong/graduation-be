from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_example.views import WisherViewSet

router = DefaultRouter()
router.register(r'wishers', WisherViewSet, basename='wisher')

urlpatterns = [
    path('wishers/<str:key>/', WisherViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='wisher-detail'),
    path('', include(router.urls)),
]
