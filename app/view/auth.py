from django.contrib.auth import login
from django.shortcuts import render, redirect

from app.form.auth import RegisterModelForm, LoginModelForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = RegisterModelForm()
    return render(request=request,
                  template_name="app/inpage/auth/register.html",
                  context={"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginModelForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request=request,
                      user=user)

                return redirect('index')
        else:
            form = LoginModelForm()
    return render(request=request,
                  template_name='app/inpage/auth/login.html',
                  context={"form": form})
