from django.urls import path
from tasks import views


app_name = 'tasks'
urlpatterns = [
    path('tasks', views.TaskView.as_view(), name='task_list'),
    path('tasks/edit/<int:pk>', views.TaskEdit.as_view(), name='task_edit'),
    path('tasks/delete/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),
    path('tasks/update-status/<int:pk>', views.TaskUpdateStatus.as_view(), name='task_update_status')
]