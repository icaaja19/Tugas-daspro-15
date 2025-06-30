from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PollResult

def index(request):
    return render(request, 'polls/index.html')

def poll_form(request):
    return render(request, 'polls/poll_form.html')

def submit_poll(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        choice = request.POST.get('choice')
        PollResult.objects.create(name=name, choice=choice)
        return redirect('show_result')
    return HttpResponse("Hanya menerima request POST.")

def show_result(request):
    results = PollResult.objects.all()
    return render(request, 'polls/result.html', {'results': results})
