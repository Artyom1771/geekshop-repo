from django.shortcuts import render , HttpResponseRedirect
from users.forms import UserLoginForm
from django.urls import reverse
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title': 'Geekshop-Авторизация','form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    return render(request, 'users/registration.html')