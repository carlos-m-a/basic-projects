from django.urls import path
from . import views
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name = 'accounts'


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name= "logout"),
    path("password_change/", PasswordChangeView.as_view(success_url = reverse_lazy('accounts:password_change_done')), name= "password_change"),
    path("password_change_done/", PasswordChangeDoneView.as_view(), name= "password_change_done"),
    path("password_reset/", PasswordResetView.as_view(success_url = reverse_lazy('accounts:password_reset_done')), name= "password_reset"),
    path("password_reset_done/", PasswordResetDoneView.as_view(), name= "password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name= "password_reset_confirm"),
    path("reset/", PasswordResetCompleteView.as_view(), name= "password_reset_complete"),

    path("profile/update/", views.update, name="update"),
    path("profile/delete/", views.delete, name="delete"),
    path("profile/", views.profile, name="profile"),
]