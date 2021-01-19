from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from Friends.forms import *
from django.contrib.auth.views import LoginView
from Friends_Album import settings


def homepage(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('slam_home')
        else:
            messages.warning(request, 'Invalid Username or Password')
            redirect('login_user')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def slam_home(request):
    # request.session.set_expiry(20)
    return render(request, 'slam_home.html')


def create_user(request):
    form = RegitrationForm()
    if request.method == 'POST':
        form = RegitrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.info(request, 'Account was created for '+user)
            return redirect('login_user')

    return render(request, 'sign_up.html',{"form": form})


def make_slam(request):
    form = SlamBookForm()
    if request.method == 'POST'or request.method == 'FILES':
        # user = request.POST.get('user')
        # print(user)
        # user = SlamBook.objects.get()
        form = SlamBookForm(request.POST, request.FILES, None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slam Saved Successfully...!!')
            return redirect('make_slam')
        else:
            return render(request, 'make_slam.html', {'error':form.errors,'form':SlamBookForm(request.POST, request.FILES, None)})
    else:
        return render(request, 'make_slam.html', {"form": form})


def view_slam(request):
    user = request.user.id
    return render(request, 'view_slam.html', {"slams": SlamBook.objects.filter(user=user)})


def view_friend(request):
    slam_no = request.GET.get('slam_no')
    slam = SlamBook.objects.get(slam_no=slam_no)
    return render(request, 'view_friend.html',{"slams": slam})


def remove_friend(request):
    slam_no = request.GET.get('slam_no')
    SlamBook.objects.get(slam_no=slam_no).delete()
    messages.success(request, 'You Lost One Slam...!!')
    return redirect('view_slam')


def edit_friend(request):
    slam_no = request.GET.get('slam_no')
    items = SlamBook.objects.get(slam_no=slam_no)
    if request.method == "POST" or request.method == "FILES":
        form = SlamBookForm(request.POST, request.FILES, instance=items)
        if form.is_valid():
            form.save()
            return redirect('view_slam')
    else:
        form = SlamBookForm(instance=items)
        return render(request, 'edit_slam.html', {"form": form})


def search_friend(request):
    search = request.GET.get("search")
    slam = SlamBook.objects.filter(my_name__icontains=search)
    return render(request, 'search.html', {"search": slam, "name": search})


def about_us(request):
    return render(request, 'about.html')

