from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_task, name='add_task'),
    path('update/', views.update_task, name='update'),
    path('list/', views.list_task, name='list'),
    path('delete/', views.delete_task, name='delete'),
]
