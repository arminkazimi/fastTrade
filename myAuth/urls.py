from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwtViews
from . import views

# router = routers.DefaultRouter()
# router.register('', views.get_user)

urlpatterns = [
    path('', views.get_user),
    path('register', views.register_user, name="register_user"),
    path('token/', jwtViews.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', jwtViews.TokenRefreshView.as_view(), name='token_refresh'),
]
