from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm


def home_page(request):
    return render(request, "user_auth/home.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.roles = ['worker']
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = RegisterForm()
    return render(request, 'user_auth/register.html', {'form': form})


def user_detail(request):
    pass


def login(request):
    pass