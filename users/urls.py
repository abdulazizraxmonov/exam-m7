from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', views.PasswordResetView.as_view(), name='password_reset'),
    path('confirm-email/', views.EmailConfirmationView.as_view(), name='email_confirmation'),
    path('confirm-email/<uidb64>/<token>/', views.EmailConfirmationVerifyView.as_view(), name='email_confirmation_verify'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]