from django.urls import path 
from . import views
urlpatterns = [ 
    path('',views.Todos),
    path('create_todo/', views.TodoCreate.as_view()),
]