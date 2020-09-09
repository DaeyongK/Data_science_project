from django.shortcuts import render
from django.views.generic import TemplateView
from Data_Science_Web_App.algorithms.average import average
# Create your views here.

class IndexView(TemplateView):
    template_name = 'Data_Science_Web_App/index.html'

class AboutView(TemplateView):
    template_name = 'Data_Science_Web_App/about.html'

def get_average(request):
    template_name = 'Data_Science_Web_App/average.html'

    if request.method == "GET":
        context={
            'num': 'Please upload a CSV file'
        }
        return render(request, template_name, context)

    csv_file = request.FILES['file_name']

    if not csv_file.name.endswith('.csv'):
        context={
            'num': 'The input type was invalid; did you make sure you used a CSV file with only numbers?'
        }
        return render(request, template_name, context)
    data_set = csv_file.read().decode('UTF-8')

    avgNum = average(data_set)

    context={
        'num': avgNum
    }
    return render(request, template_name, context)
