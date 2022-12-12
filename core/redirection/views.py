from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Links
from django.http import HttpResponseRedirect

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

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'redirection/signin.html', {'errors': 1})
    else:
        return render(request, 'redirection/signin.html', {'errors': 0})

def redirector(request, slug):
    #print(dir(request))
    link = Links.objects.get(slug=slug)
    link.counter = link.counter + 1
    link.save()
    return HttpResponseRedirect(link.url_link)

@login_required
def profile(request):
    links = Links.objects.filter(user=request.user)

    return render(request, 'redirection/profile.html', {'links' : links})