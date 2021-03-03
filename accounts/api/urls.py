from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.api import views

router = DefaultRouter()

router.register('register_user', views.UserCreateApiView, basename='users')
#router.register('verify_user', views.UserVerifyApiView, basename='verify_user')



urlpatterns = [
    path('', include(router.urls)),
]