from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Tasks

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    usr_id = request.user.get_username()
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            tsk_title = form.cleaned_data['tsk_title']
            tsk_desc = form.cleaned_data['tsk_desc']
            tsk_priority = form.cleaned_data['tsk_priority']
            due_date = form.cleaned_data['due_date']
            due_time = form.cleaned_data['due_time']
            is_completed = form.cleaned_data['is_completed']

            tasks = Tasks(usr_id=usr_id, tsk_title=tsk_title, tsk_desc=tsk_desc, tsk_priority=tsk_priority, due_date=due_date, due_time=due_time, is_completed=is_completed)

            tasks.save()
            form = TaskForm()
    else:
        form = TaskForm()

    tasks_data = Tasks.objects.filter(usr_id=usr_id).values()

    context = {
        'form': form,
        'tasks': tasks_data
    }
    return render(request, 'home.html', context)
    # return render(request, 'home.html')

