from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Tasks

# Create your views here.
@login_required(login_url='/accounts/login/')
def task(request, id):
    usr_id = request.user.get_username()
    task = Tasks.objects.get(usr_id=usr_id, tsk_id=id)
    if request.method == 'POST':
        if task:
            form = TaskForm(instance=task)
            context = {
                'form': form,
                'task': task
            }
            return render(request, 'task.html', context)
    return render(request, '404.html')


