# dashboard_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import DataPoint, DataPoint2, DataPoint3

def dashboard(request):
    data_points = DataPoint.objects.all()
    data_points2 = DataPoint2.objects.all()  # Updated variable name
    data_points3 = DataPoint3.objects.all()  # Updated variable name
    labels = [point.label for point in data_points]
    values = [point.value for point in data_points]

    context = {
        'labels': labels,
        'values': values,
        'labels2': [point.label for point in data_points2],  # Add labels for DataPoint2
        'values2': [point.value for point in data_points2],  # Add values for DataPoint2
        'labels3': [point.label for point in data_points3],  # Add labels for DataPoint3
        'values3': [point.value for point in data_points3],  # Add values for DataPoint3
    }

    return render(request, 'dashboard/dashboard.html', context)

def get_data(request):
    data_points = DataPoint.objects.all()
    data = {'labels': [point.label for point in data_points], 'values': [point.value for point in data_points]}
    return JsonResponse(data)

def get_data2(request):
    data_points = DataPoint2.objects.all()
    data = {'labels': [point.label for point in data_points], 'values': [point.value for point in data_points]}
    return JsonResponse(data)

def get_data3(request):
    data_points = DataPoint3.objects.all()
    data = {'labels': [point.label for point in data_points], 'values': [point.value for point in data_points]}
    return JsonResponse(data)

def about(request):
    return render(request, 'dashboard/about.html')
