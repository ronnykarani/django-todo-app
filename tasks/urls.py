from django.urls import path
from . import views
from .views import TaskList

urlpatterns = [
    # path('', views.index, name='list'),
    path('', TaskList.as_view(), name='tasks'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete')
]  