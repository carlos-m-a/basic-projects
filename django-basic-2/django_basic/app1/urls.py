from django.urls import path
from . import views


app_name = 'app1'


urlpatterns = [
    path("books", views.get_books, name="get_books"),
]