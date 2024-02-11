from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# Create your views here.


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        print(request.session.get_expiry_date)
        return redirect('home')

    if request.method == 'POST':
        valuenext = request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if remember_me:
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            else:
                request.session.set_expiry(0)
            login(request, user)
            if valuenext == '':
                return redirect('home')
            else:
                return redirect(valuenext)
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}

    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'signup'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def location(request):
    return render(request, 'location.html')
