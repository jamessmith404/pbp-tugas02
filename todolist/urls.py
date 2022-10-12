# TODO: Implement Routings Here
from django.urls import path
from todolist.views import delete_task, show_todolist
from todolist.views import register, login_user, logout_user, create_task, delete_task, done_task, undone_task #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import show_todolist_json, add_task_ajax, delete_task_ajax, done_task_ajax, undone_task_ajax


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', create_task, name="create_task"),
    path('delete_task/<int:id>', delete_task, name="delete_task"),
    path('done_task/<int:id>', done_task, name="done_task"),
    path('undone_task/<int:id>', undone_task, name="undone_task"),
    path('json', show_todolist_json, name="show_todolist_json"),
    path('add', add_task_ajax, name="add_task_ajax"),
    path('delete/<int:id>', delete_task_ajax, name="delete_task_ajax"),
    path('done_task_ajax/<int:id>', done_task_ajax, name="done_task_ajax"),
    path('undone_task_ajax/<int:id>', undone_task_ajax, name="undone_task_ajax"),
]