from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register(r'authentication-token', views.AuthTokenViewSet, base_name='authentication-token')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/$', views.TestAuthView.as_view()),
]
