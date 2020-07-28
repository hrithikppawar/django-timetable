from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TableForm, CreateUserForm
from .models import Day
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user)
            return redirect('login')
    content = {
        'form': form
    }
    return render(request, 'table/register.html', content)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password is not correct')

    content = {}
    return render(request, 'table/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    # FORM PART
    if request.method == 'POST':
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        subject = request.POST.get('subject')
        Day.objects.create(user=request.user, day_name=day,
                           start_time=start_time, end_time=end_time, subject=subject)

    Days = {
        'Monday': Day.objects.filter(user=request.user).filter(day_name='Monday').order_by('start_time'),
        'Tuesday': Day.objects.filter(user=request.user).filter(day_name='Tuesday').order_by('start_time'),
        'Wednesday': Day.objects.filter(user=request.user).filter(day_name='Wednesday').order_by('start_time'),
        'Thursday': Day.objects.filter(user=request.user).filter(day_name='Thursday').order_by('start_time'),
        'Friday': Day.objects.filter(user=request.user).filter(day_name='Friday').order_by('start_time'),
        'Saturday': Day.objects.filter(user=request.user).filter(day_name='Saturday').order_by('start_time'),
        'Sunday': Day.objects.filter(user=request.user).filter(day_name='Sunday').order_by('start_time')
    }

    content = {
        'Days': Days
    }
    return render(request, 'table/dashboard.html', content)


@login_required(login_url='login')
def deleteLecture(request, id):
    lecture = Day.objects.get(id=id)
    if request.method == 'POST':
        lecture.delete()
        return redirect('/')
    content = {
        'lecture': lecture
    }
    return render(request, 'table/delete.html', content)
