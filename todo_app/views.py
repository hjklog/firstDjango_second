from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Todo

# Create your views here.
class TodoCreate(LoginRequiredMixin ,CreateView):
    model=Todo
    fields=['todo','description','important']

def Todos(request):
    todos = Todo.objects.all().order_by('-pk')
    return render(
        request,
        'todo_app/todos.html',
        {
            'todos':todos,
        }
    )