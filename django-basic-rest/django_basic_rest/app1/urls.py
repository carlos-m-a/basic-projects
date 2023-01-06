from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('notes5', views.NoteViewSet)

urlpatterns = [
    path('todos/', views.TodoListApiView.as_view()),
    path('todos/<int:todo_id>/', views.TodoDetailApiView.as_view()),

    path('notes1/', views.note_list),
    path('notes1/<int:note_id>/', views.note_detail),

    path('notes2/', views.NoteListApiView.as_view()),
    path('notes2/<int:note_id>/', views.NoteDetailApiView.as_view()),

    path('notes3/', views.NoteListGeneric.as_view()),
    path('notes3/<int:pk>/', views.NoteDetailGeneric.as_view()),

    path('notes4/', views.NoteListConcrete.as_view()),
    path('notes4/<int:pk>/', views.NoteDetailConcrete.as_view()),

    path('', include(router.urls)),

    path('checking-auth-class/', views.ClassBasedView.as_view()),

    path('checking-auth-function/', views.function_based_view)

]