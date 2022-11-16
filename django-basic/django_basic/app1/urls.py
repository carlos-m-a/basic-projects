from django.urls import path
from . import views


app_name = 'app1'


urlpatterns = [
    path("home", views.home, name="home"),
    path("my_model_detail/<int:pk>/", views.MyModelDetailView.as_view(), name="my_model_detail"),
    path("my_model_list/", views.MyModelListView.as_view(), name="my_model_list"),
    path("my_model_create/", views.MyModelCreateView.as_view(), name="my_model_create"),
    path("my_model_update/<int:pk>/", views.MyModelUpdateView.as_view(), name="my_model_update"),
    path("my_model_delete/<int:pk>/", views.MyModelDeleteView.as_view(), name="my_model_delete"),
]