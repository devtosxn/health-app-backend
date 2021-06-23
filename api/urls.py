from django.urls import path, include

from api.views.login import LoginView
from api.views.register_view import RegisterUserView
from api.views.verify_otp import VerifyOtp
from api.views.forgot_password import ForgotPasswordView
from api.views.resetpassword import PasswordReset 


urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('otps/verify/', VerifyOtp.as_view(), name='verify-otp'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('passwords/forgot/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('passwords/reset/',PasswordReset.as_view(), name='reset-password'),
]
