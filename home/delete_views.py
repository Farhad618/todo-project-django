from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Tasks

# Create your views here.
@login_required(login_url='/accounts/login/')
def delete(request, id):
    if request.method == 'POST':
        usr_id = request.user.get_username()
        task = Tasks.objects.get(usr_id=usr_id, tsk_id=id)
        if task:
            task.delete()
            return HttpResponseRedirect("/")
    return render(request, '404.html')

    # return HttpResponseRedirect("/")
    # return render(request, 'home.html', context)
    # return render(request, 'home.html')


