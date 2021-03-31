from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from apps.forms import UserForm
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(redirect_field_name='user_login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required(redirect_field_name='user_login')
def news(request):
    response = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=2b97df78d7fc4b8593abe60990851f8a")
    articles = response.json()['articles']
    content = {'articles':articles}
    return render(request, 'news.html', content)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, "registration.html", {'registered':registered, 'user_form':user_form})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone try to login and failed")
            print(f"username: {username}\npassword: {password}")
            return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request, 'login.html', {})

def tester(request):
    return render(request, "tester.html", {})