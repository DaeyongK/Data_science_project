from django.shortcuts import render
from django.views.generic import TemplateView
from Data_Science_Web_App.algorithms.average import average, median
from Data_Science_Web_App.algorithms.xyplot import xyplot
from . import forms
import os
import pandas
import mpld3

# Create your views here.

graph_path = os.path.abspath('media/graphs')


class IndexView(TemplateView):
    template_name = 'Data_Science_Web_App/index.html'

class AboutView(TemplateView):
    template_name = 'Data_Science_Web_App/about.html'

def get_average(request):
    template_name = 'Data_Science_Web_App/average.html'


    if request.method == "GET":
        context={
            'num': 'Please upload a CSV file',
            'left': 'Please upload a CSV file',
            'mid': 'Please upload a CSV file',
            'right': 'Please upload a CSV file'
        }
        return render(request, template_name, context)
    #Vulnerability
    csv_file = request.FILES['file_name']

    if not csv_file.name.endswith('.csv'):
        context={
            'num': 'The input type was invalid; did you make sure you used a CSV file with only numbers?'
        }
        return render(request, template_name, context)
    data_set = csv_file.read().decode('UTF-8')

    avgNum = average(data_set)
    left,mid,right = median(data_set)



    context = {
        'num': avgNum,
        'left': left,
        'mid': mid,
        'right': right
    }
    return render(request, template_name, context)










def plot(request):
    template_name = 'Data_Science_Web_App/plot.html'


    # if request.method == "GET":
    #     context={
    #
    #     }
    #     return render(request, template_name, context)
    # #Vulnerability

    form = forms.PlotChartForm()
    context={
        'success': False,
        'form': form,
        'img': 'Please fill out the required fields!'
    }
    if request.method == 'POST':

        form = forms.PlotChartForm(request.POST, request.FILES)

        if form.is_valid():

            data_file = form.cleaned_data['data_file']
            xIndex = form.cleaned_data['xIndex']
            yIndex = form.cleaned_data['yIndex']
            xLabel = form.cleaned_data['xLabel']
            yLabel = form.cleaned_data['yLabel']
            title = form.cleaned_data['title']
            lowerX = form.cleaned_data['lowerX']
            upperX = form.cleaned_data['upperX']
            lowerY = form.cleaned_data['lowerY']
            upperY = form.cleaned_data['upperY']
            alphaVal = form.cleaned_data['alphaVal']

            if not data_file.name.endswith('.csv'):
                context={
                    'success': False,
                    'form': form,
                    'img': 'The input type was invalid; did you make sure you used a CSV file?'
                }
                return render(request, template_name, context)

            data_set = pandas.read_csv(data_file)
            # .decode('UTF-8')


            xR = [lowerX, upperX]
            yR = [lowerY, upperY]
            # print(type(xIndex))
            # print(xIndex, yIndex, xLabel, yLabel, title, xR, yR, alphaVal)
            # try:
            figure = xyplot(data_set, xIndex, yIndex, xLabel, yLabel, title, xR, yR, alphaVal)

            graph_image = 'graph.png'

            figure.savefig(os.path.join(graph_path, graph_image))
            # figure = mpld3.fig_to_html(figure)
            # except:
            #     figure = 'Something went wrong! Please make sure all of your inputs are valid inputs'

            context = {
                'success': True,
                'form': form,
                'img': 'Data_Science_Web_App/graphs/graph.png'
            }


    return render(request, template_name, context)
