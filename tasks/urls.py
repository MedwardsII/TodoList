from django.urls import path
from tasks import views


app_name = 'tasks'
urlpatterns = [
    path('tasks', views.task_create, name='task_list'),
    path('tasks/edit/<int:pk>', views.task_edit, name='task_edit'),
    path('tasks/delete/<int:pk>', views.task_delete, name='task_delete'),
    path('tasks/update-status/<int:pk>', views.task_update_stats, name='task_update_status')
]