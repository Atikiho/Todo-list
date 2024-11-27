from django.urls import path

from todo_list.views import (
    TaskList,
    TaskDelete,
    TaskUpdate,
    TaskCreate,
    TagCreate,
    TagUpdate,
    TagDelete,
    TagList,
    task_action
)

app_name = "todo-list"

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("tasks/delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
    path("tasks/update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("tasks/create/", TaskCreate.as_view(), name="task-create"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path("tags/delete/<int:pk>/", TagDelete.as_view(), name="tag-delete"),
    path("tags/update/<int:pk>/", TagUpdate.as_view(), name="tag-update"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("tasks/action/<int:pk>", task_action, name="task-action"),
]


