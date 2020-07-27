from django.shortcuts import render
from django.http import HttpResponse
from .forms import TableForm
from .models import Day
# Create your views here.


def index(request):
    # FORM PART
    form = TableForm()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()

    Days = {
        'Monday': Day.objects.filter(day_name='Monday').order_by('start_time'),
        'Tuesday': Day.objects.filter(day_name='Tuesday').order_by('start_time'),
        'Wednesday': Day.objects.filter(day_name='Wednesday').order_by('start_time'),
        'Thursday': Day.objects.filter(day_name='Thursday').order_by('start_time'),
        'Friday': Day.objects.filter(day_name='Friday').order_by('start_time'),
        'Saturday': Day.objects.filter(day_name='Saturday').order_by('start_time'),
        'Sunday': Day.objects.filter(day_name='Sunday').order_by('start_time')
    }

    content = {
        'form': form,
        'Days': Days
    }
    return render(request, 'table/dashboard.html', context=content)
