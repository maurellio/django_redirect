from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


# Create your views here.

def index(request):
    return render(request, 'redirection/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        #print(form.errors)
        if form.is_valid():
            #print(form.data)
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'redirection/signup.html', {'form' : form})


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            print('kek')
            login(request, user)
            return redirect('index')
        else:
            print('notkek')
            return render(request, 'redirection/signin.html', {'errors': 1})
    else:
        print('notkek2')
        return render(request, 'redirection/signin.html', {'errors': 0})
