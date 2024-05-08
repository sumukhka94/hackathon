from django.shortcuts import render
from django.http import JsonResponse
import json

def chart(request):
    labels = [i for i in range(1,100000,20000)]
    my_data = {'label': 'Percentage', 'values': [5, 10, 15, 30, 54]}
    return render(request, 'chart.html', {'data': my_data ,'labels' : labels})

#toggle

def get_chart_data(request):
    selected_dealer = request.GET.get('selected_dealer')
    selected_analytics = request.GET.get('selected_analytics')

    if selected_dealer == 'data1':
        if selected_analytics == 'analytics1':
            data = {
                'labels': [str(i) + 'k' for i in range(1, 10)],
                'datasets': [{
                    'label': 'Dealer 1 with No Anaylitcs ',
                    'data': [12, 13, 17, 19, 21, 21, 21, 21, 17, 23],
                    'borderColor': 'red',
                    'backgroundColor': 'red',
                    'fill': False
                }]
            }
        elif selected_analytics == 'analytics2':
            data = {
                'labels': [str(i) + 'k' for i in range(1, 10)],
                'datasets': [
                    {
                        'label': 'Dealer 1 with Analytics',
                        'data': [20, 24, 32, 32, 38, 42, 43, 44, 46, 45],
                        'borderColor': 'green',
                        'backgroundColor': 'green',
                        'fill': False
                    },
                    {
                        'label': 'Dealer 1 with No Anaylitcs ',
                        'data': [12, 13, 17, 19, 21, 21, 21, 21, 17, 3],
                        'borderColor': 'red',
                        'backgroundColor': 'red',
                        'fill': False
                    }
                ]
            }
        else:
            data = {
                'labels': [],
                'datasets': []
            }
    elif selected_dealer == 'data2':
        if selected_analytics == 'analytics1':
            data = {
                'labels': [str(i) + 'k' for i in range(1, 10)],
                'datasets': [{
                    'label': 'Dealer 2 with No Anaylitcs',
                    'data': [12, 13, 17, 14, 21, 21, 21, 21, 17, 23],
                    'borderColor': 'red',
                    'backgroundColor': 'red',
                    'fill': False
                }]
            }
        elif selected_analytics == 'analytics2':
            data = {
                'labels': [str(i) + 'k' for i in range(1, 10)],
                'datasets': [{
                    'label': 'Dealer 2 with Analytics',
                    'data': [23, 21, 25, 30, 36, 37, 40, 42, 45, 43],
                    'borderColor': 'green',
                    'backgroundColor': 'green',
                    'fill': False
                },
                {
                    'label': 'Dealer 2 with No Anaylitcs',
                    'data': [12, 13, 17, 14, 21, 21, 21, 21, 17, 23],
                    'borderColor': 'red',
                    'backgroundColor': 'red',
                    'fill': False
                }]
            }
        else:
            data = {
                'labels': [],
                'datasets': []
            }
    else:
        data = {
            'labels': [],
            'datasets': []
        }
        
    return JsonResponse(data)


def chart_view(request):
    return render(request, 'toggle-chart.html')