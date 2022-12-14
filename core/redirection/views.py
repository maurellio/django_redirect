from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import SignUpForm, CreateLink
from django.contrib.auth.decorators import login_required
from .models import Links, API_token, User
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout
from .serializers import LinksSerializer

from rest_framework.authtoken.models import Token
# Create your views here.

def index(request):
    return render(request, 'redirection/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
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
            return redirect('profile')
        else:
            return render(request, 'redirection/signin.html', {'errors': 1})
    else:
        return render(request, 'redirection/signin.html', {'errors': 0})

def redirector(request, slug):
    link = Links.objects.get(slug=slug)
    link.counter = link.counter + 1
    link.save()
    return HttpResponseRedirect(link.url_link)

@login_required
def profile(request):
    links = Links.objects.filter(user=request.user)

    return render(request, 'redirection/profile.html', {'links' : links})

@login_required
def create_link(request):
    if request.method == 'GET':
        form = CreateLink()
    else:
        form = CreateLink(request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.save()
            return redirect('profile')

    return render(request, 'redirection/create_link.html', {'form' : form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def delete_link(request, slug):
    Links.objects.get(slug=slug).delete()
    return redirect('profile')

@login_required
def create_token(request):
    token = Token.objects.create(user=request.user)
    API_token.object.create(user=request.user, token=token)
    print(token)
    return redirect('profile')

# API realization
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def links_api(request):
    if request.method == 'GET':
        links = Links.objects.filter(user=request.user)
        serializer = LinksSerializer(links, many=True)
        return JsonResponse({'links' : serializer.data})

    if request.method == 'POST':
        serializer = LinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_links_api(request, slug):
    try:
        link = Links.objects.get(slug=slug)
    except Links.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LinksSerializer(link)
        return Response(serializer.data)
    elif request.method == 'PUT':
        LinksSerializer(data=request.data)

    elif request.method == 'DELETE':
        pass