from django.urls import path
# from . import views
from .views import TaskDetail, TaskList, TaskCreate

urlpatterns = [
    # path('', views.index, name='list'),
    # path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    # path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),

]  