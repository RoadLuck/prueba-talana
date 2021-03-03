from django.urls import path, include
from rest_framework.routers import SimpleRouter
from accounts.api import views

router = SimpleRouter()

router.register('register_user', views.UserCreateApiView, basename='users')
#router.register()



urlpatterns = [
    path('', include(router.urls)),
    path('verify_user', views.verify_account),
    path('generate_winner', views.generate_winner),
]