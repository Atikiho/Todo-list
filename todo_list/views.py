from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_list.models import Task, Tag


class TaskList(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"


class TaskCreate(generic.CreateView):
    model = Task
    template_name = "todo_list/form.html"
    success_url = reverse_lazy("todo-list:task-list")
    fields = "__all__"


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-list:task-list")


class TaskUpdate(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo_list/form.html"
    success_url = reverse_lazy("todo-list:task-list")


class TagList(generic.ListView):
    model = Tag
    template_name = "todo_list/tags.html"
    success_url = reverse_lazy("todo-list:task-list")


class TagCreate(generic.CreateView):
    model = Tag
    template_name = "todo_list/form.html"
    success_url = reverse_lazy("todo-list:tag-list")
    fields = "__all__"


class TagDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo-list:tag-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_list/form.html"
    success_url = reverse_lazy("todo-list:tag-list")


def task_action(request, pk: int):
    task = Task.objects.get(id=pk)
    task.state = not task.state
    task.save()
    return redirect(reverse("todo-list:task-list"))
