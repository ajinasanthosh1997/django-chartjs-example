# dashboard_app/views.py
from django.shortcuts import render
from .models import DataPoint
from django.http import JsonResponse

def dashboard(request):
    data_points = DataPoint.objects.all()
    labels = [point.label for point in data_points]
    values = [point.value for point in data_points]

    context = {
        'labels': labels,
        'values': values,
    }

    return render(request, 'dashboard/dashboard.html', context)

def get_data(request):
    data_points = DataPoint.objects.all()
    data = {'labels': [point.label for point in data_points], 'values': [point.value for point in data_points]}
    return JsonResponse(data)
