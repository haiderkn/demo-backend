"""
URL mappings for the user API
"""
from django.urls import path
from user import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'user'

urlpatterns = [
    path('user/register/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
    path('health-check/', views.health_check, name='health-check'),
]
