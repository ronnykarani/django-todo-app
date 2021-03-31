from django.urls import path
# from . import views
from .views import CustomLoginView, TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete


urlpatterns = [
    # path('', views.index, name='list'),
    # path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    # path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]  