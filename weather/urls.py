from django.urls import path, include
from weather import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('descriptions', views.DescriptionViewSet)

urlpatterns = [
    path('', include(router.urls))
]