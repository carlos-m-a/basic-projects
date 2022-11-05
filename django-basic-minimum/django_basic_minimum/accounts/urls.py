from django.urls import path
from . import views
from .views import RegisterView, NewLoginView, NewLogoutView, NewPasswordResetView, NewPasswordResetConfirmView, NewPasswordResetDoneView, NewPasswordResetCompleteView, NewPasswordChangeView, NewPasswordChangeDoneView


app_name = 'accounts'


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", NewLoginView.as_view(), name="login"),
    path("logout/", NewLogoutView.as_view(), name= "logout"),
    path("password_change/", NewPasswordChangeView.as_view(), name= "password_change"),
    path("password_change_done/", NewPasswordChangeDoneView.as_view(), name= "password_change_done"),
    path("password_reset/", NewPasswordResetView.as_view(), name= "password_reset"),
    path("password_reset_done/", NewPasswordResetDoneView.as_view(), name= "password_reset_done"),
    path("reset/<uidb64>/<token>/", NewPasswordResetConfirmView.as_view(), name= "password_reset_confirm"),
    path("reset/", NewPasswordResetCompleteView.as_view(), name= "password_reset_complete"),

    path("profile/", views.profile, name="profile"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]