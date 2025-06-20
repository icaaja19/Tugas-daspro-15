from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Settings, Question, Choice
from .forms import SettingsForm

# =======================
# Halaman Statis / Info
# =======================

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def profile(request):
    return HttpResponse("Ini adalah halaman profile.")

def contact(request):
    return HttpResponse("Ini adalah halaman contact.")

def address(request):
    return HttpResponse("Ini adalah halaman address.")

def phone(request):
    return HttpResponse("Ini adalah halaman phone.")

# =======================
# Settings - Tampilan dan Edit
# =======================
def settings_view(request):
    settings_data = Settings.objects.all()
    output = "<br>".join([f"{s.name}: {s.value}" for s in settings_data])
    return HttpResponse(f"<h1>Settings:</h1><p>{output}</p>")

def edit_settings(request):
    settings_list = Settings.objects.all()

    if request.method == "POST":
        for setting in settings_list:
            new_value = request.POST.get(setting.name)
            if new_value is not None:
                setting.value = new_value
                setting.save()
        return redirect("edit_settings")

    context = {"settings": settings_list}
    return render(request, "edit_settings.html", context)

# =======================
# Halaman Utama Polling
# =======================
def html_index(request):
    questions = Question.objects.all().order_by('-pub_date')
    return render(request, 'polls/index.html', {'questions': questions})


# =======================
# Polling: Detail, Vote, Hasil
# =======================
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Tampilkan form lagi dengan error message
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Anda belum memilih atau pilihan tidak tersedia.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # ✅ Redirect ke hasil
        return redirect("polls:results", question_id=question.id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


