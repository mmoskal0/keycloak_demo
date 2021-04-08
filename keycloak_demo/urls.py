from django.urls import path, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from demo import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
]