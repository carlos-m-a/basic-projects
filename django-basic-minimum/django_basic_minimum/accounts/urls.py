from django.urls import path
from . import views
from .views import RegisterView, UpdateView

app_name = 'accounts'


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/update/", views.update, name="update"),
    path("profile/delete/", views.delete, name="delete"),
    path("profile/", views.profile, name="profile"),
]