from django.urls import path
from rest_framework.routers import SimpleRouter

from words import views

router = SimpleRouter()
router.register(r'words', views.WordViewSet)

urlpatterns = [
]

urlpatterns += router.urls
