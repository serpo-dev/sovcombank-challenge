from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from account.views import LoginUser, UsersAccount, UserDetails, RegisterUser, UserTransaction, currency_period_days

app_name = 'accounts'

urlpatterns = [
    path('user/register', RegisterUser.as_view(), name='user-register'),
    path('user/details', UserDetails.as_view(), name='user-detail'),
    path('user/login', LoginUser.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('user/accounts', UsersAccount.as_view(), name='user-account'),
    path('user/transactions', UserTransaction.as_view(), name='user-transactions'),
    path('currency/period/<int:days>/<source>/', currency_period_days)
]