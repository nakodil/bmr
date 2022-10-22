from django.shortcuts import render
from .forms import BmrForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "GET":
        form = BmrForm()
        return render(request, "bmr/index.html", {"form": form})
    else:
        form = BmrForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data["gender"]
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            age = form.cleaned_data["age"]
            activity = form.cleaned_data["activity"]
            bmr = 100  # хардкод, нужен рассчет 
            return render(request, "bmr/result.html", {"bmr": bmr})
        else:
            print("форма невалидна!!!!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponse("нет")
