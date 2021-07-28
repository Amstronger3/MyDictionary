from django.urls import path
from rest_framework.routers import SimpleRouter

from words import views

router = SimpleRouter()
router.register(r'words', views.WordViewSet)
router.register(r'words/create', views.WordViewSet)
router.register(r'words/update', views.WordViewSet)
router.register(r'words/<int:pk>/delete', views.WordViewSet)

urlpatterns = [
    # path('words/', views.WordView.as_view()),
]

urlpatterns += router.urls
