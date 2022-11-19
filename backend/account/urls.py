from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from account.views import LoginUser, UsersAccount, UserDetails, RegisterUser

app_name = 'account'

urlpatterns = [
    path('user/register', RegisterUser.as_view(), name='user-register'),
    # # path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', UserDetails.as_view(), name='user-detail'),
    path('user/login', LoginUser.as_view(), name='user-login'),
    # path('user/password_reset', reset_password_request_token, name='password-reset'),
    # path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('user/account', UsersAccount.as_view(), name='user-account')
]