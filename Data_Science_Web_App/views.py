from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import default_storage
from Data_Science_Web_App.algorithms.variable_stats import variable_stats, strWSpace
from Data_Science_Web_App.algorithms.xyplot import xyplot
from Data_Science_Web_App.algorithms.histo import histo
from Data_Science_Web_App.algorithms.interp import interp
from Data_Science_Web_App.algorithms.key import generate_key
from Data_Science_Web_App.algorithms.locator import locate
from django.http import HttpResponse
from . import forms
from Data_Science_Web_App.models import TemporaryFile
import os
import pandas
import mpld3
import csv
import random
import string
from Data_Science_Project.settings import MEDIA_ROOT
# from Data_Science_Project.settings import STATIC_ROOT, TEMPLATE_DIR


#Media file DIR
graph_path = os.path.abspath('media/graphs')

# Create your views here.


#CBVs
class IndexView(TemplateView):
    template_name = 'Data_Science_Web_App/index.html'

class AboutView(TemplateView):
    template_name = 'Data_Science_Web_App/about.html'

class MainPageView(TemplateView):
    template_name = 'Data_Science_Web_App/main_page.html'



#Function-based views
def variable_statistics(request):

    template_name = 'Data_Science_Web_App/variable_stats.html'


    #Default rendering
    if request.method == "GET":
        context={
            'num': 'Please upload a CSV file',
            'left': 'Please upload a CSV file',
            'mid': 'Please upload a CSV file',
            'right': 'Please upload a CSV file',
            'mode': 'Please upload a CSV file',
            'std': 'Please upload a CSV file',
            'std1lower': 'Please upload a CSV file',
            'std1upper': 'Please upload a CSV file',
            'std2lower': 'Please upload a CSV file',
            'std2upper': 'Please upload a CSV file',
            'std3lower': 'Please upload a CSV file',
            'std3upper': 'Please upload a CSV file',
            'variance': 'Please upload a CSV file',
            'Q1': 'Please upload a CSV file',
            'Q3': 'Please upload a CSV file',
            'IQR': 'Please upload a CSV file',
            'range': 'Please upload a CSV file'
        }
        return render(request, template_name, context)

    #Checking if user filled out both areas
    try:
        csv_file = request.FILES['file_name']
        csv_text = request.POST.get('csv_text')
        key_field = request.POST.get('key_field')
        #But if csv_text and key_field is empty which means that the textarea was left alone,
        if csv_text == "" and key_field == "":

            csv_file = request.FILES['file_name']

            #Checking if it's an actual csv file
            if not csv_file.name.endswith('.csv'):
                context={
                    'num': 'The input type was invalid; did you make sure you used a CSV file with only numbers?'
                }
                return render(request, template_name, context)

            data_set = csv_file.read().decode('UTF-8')

        #This will run if the user provided data for both inputs
        else:
            context={
                'num': 'Please enter your data into only one of the fields'
            }

            return render(request, template_name, context)


    #This will run if the program fails to read the file because it isn't there. It goes on to read the data in the textarea
    except:
        csv_text = request.POST.get('csv_text')
        key_field = request.POST.get('key_field')
        #This will run only if the user pressed upload without providing any data
        if csv_text == "" and key_field == "":
            context={
                'num': 'Please provide an input'
            }
            return render(request, template_name, context)

        elif csv_text != "" and key_field == "":
            data_set = csv_text
        elif csv_text == "" and key_field != "":
            try:
                csv_file = locate(key_field)
                data_set = csv_file.read().decode('UTF-8')
            except:
                context={
                    'num': 'Looks like your key was invalid'
                }
                return render(request, template_name, context)
        elif csv_text != "" and key_field != "":
            context={
                'num': 'Please enter your data into only one of the fields'
            }

            return render(request, template_name, context)

    #Running the algorithms on the data_set
    try:
        avgNum, mode_return, left, mid, right, std, std1lower, std1upper, std2lower, std2upper, std3lower, std3upper, variance, Q1, Q3, IQR, range =  variable_stats(data_set)
        if mode_return == None:
            modeNum = "There was no mode in the given data"
        else:
            modeNum = " ".join(list(map(strWSpace, mode_return)))[:-2]


    #This will run if one of the algorithms failed; at this point the only possible reason is because the data was not formatted properly
    except:
        context={
            'num': 'Please format your data properly'
        }
        return render(request, template_name, context)


    #This only runs if everything was successful. It renders the view after the user presses upload
    context = {
        'num': avgNum,
        'left': left,
        'mid': mid,
        'right': right,
        'mode': modeNum,
        'std': std,
        'std1lower': std1lower,
        'std1upper': std1upper,
        'std2lower': std2lower,
        'std2upper': std2upper,
        'std3lower': std3lower,
        'std3upper': std3upper,
        'variance': variance,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'range': range
    }

    return render(request, template_name, context)


























def plot(request):

    #All basic variables
    template_name = 'Data_Science_Web_App/plot.html'
    form = forms.PlotChartForm()
    context={
        'success': False,
        'form': form,
        'error_message': 'Please fill out the required fields!'
    }


    if request.method == 'POST':

        form = forms.PlotChartForm(request.POST, request.FILES)


        #Checking if all fields are valid
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
                    'error_message': 'The input type was invalid; did you make sure you used a CSV file?'
                }

                return render(request, template_name, context)


            #Reading data_file with pandas, so that data_set is now a pandas dataframe
            data_set = pandas.read_csv(data_file)
            xR = [lowerX, upperX]
            yR = [lowerY, upperY]

            #Trying to create a plot with given fields, and if successful save it

            try:

                figure = xyplot(data_set, xIndex, yIndex, xLabel, yLabel, title, xR, yR, alphaVal)

                graph_image = 'graph.png'

                figure.savefig(os.path.join(graph_path, graph_image))

            except:

                #Returning error message on failure
                context={
                    'success': False,
                    'form': form,
                    'error_message': 'Something went wrong with creating the graph. Did you format your data properly?'
                }

                return render(request, template_name, context)

            #The final context dictionary with success being true. In this case, the error_message shouldn't pop up
            context = {
                'success': True,
                'form': form,
                'error_message': 'The graph should have been here, but something went wrong'
            }

    return render(request, template_name, context)

















#Add in context later
def gaussian(request):

    template_name = 'Data_Science_Web_App/gaussian.html'
    return render(request, template_name)


def density(request):

    template_name = 'Data_Science_Web_App/density.html'
    return render(request, template_name)



def transformation(request):

    template_name = 'Data_Science_Web_App/transformation.html'
    return render(request, template_name)
















def histoplot(request):

    #All basic variables
    template_name = 'Data_Science_Web_App/histo.html'
    form = forms.HistoForm()
    context={
        'success': False,
        'form': form,
        'error_message': 'Please fill out the required fields!'
    }


    if request.method == 'POST':

        form = forms.HistoForm(request.POST, request.FILES)


        #Checking if all fields are valid
        if form.is_valid():

            data_file = form.cleaned_data['data_file']
            colN = form.cleaned_data['colN']
            xLabel = form.cleaned_data['xLabel']
            yLabel = form.cleaned_data['yLabel']
            title = form.cleaned_data['title']
            lowerX = form.cleaned_data['lowerX']
            upperX = form.cleaned_data['upperX']
            lowerY = form.cleaned_data['lowerY']
            upperY = form.cleaned_data['upperY']
            hStyle = form.cleaned_data['hStyle']
            binS = form.cleaned_data['binS']
            densYes = form.cleaned_data['densYes']


            if not data_file.name.endswith('.csv'):

                context={
                    'success': False,
                    'form': form,
                    'error_message': 'The input type was invalid; did you make sure you used a CSV file?'
                }

                return render(request, template_name, context)


            #Reading data_file with pandas, so that data_set is now a pandas dataframe
            data_set = pandas.read_csv(data_file)
            xR = [lowerX, upperX]
            yR = [lowerY, upperY]

            #Trying to create a plot with given fields, and if successful save it
            try:

                figure = histo(data_set, colN, xLabel, yLabel, title, xR, yR, hStyle, binS, densYes)

                graph_image = 'histograph.png'

                figure.savefig(os.path.join(graph_path, graph_image))

            except:

                #Returning error message on failure
                context={
                    'success': False,
                    'form': form,
                    'error_message': 'Something went wrong with creating the graph. Did you format your data properly?'
                }

                return render(request, template_name, context)

            #The final context dictionary with success being true. In this case, the error_message shouldn't pop up
            context = {
                'success': True,
                'form': form,
                'error_message': 'The graph should have been here, but something went wrong'
            }

    return render(request, template_name, context)










def interpolation(request):
    #All basic variables
    template_name = 'Data_Science_Web_App/interpolation.html'
    form = forms.InterpolationForm()
    context={
        'success': False,
        'form': form,
        'error_message': 'Please fill out the required fields!'
    }


    if request.method == 'POST':

        form = forms.InterpolationForm(request.POST, request.FILES)


        #Checking if all fields are valid
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
            iKind = form.cleaned_data['iKind']

            if not data_file.name.endswith('.csv'):

                context={
                    'success': False,
                    'form': form,
                    'error_message': 'The input type was invalid; did you make sure you used a CSV file?'
                }

                return render(request, template_name, context)


            #Reading data_file with pandas, so that data_set is now a pandas dataframe
            data_set = pandas.read_csv(data_file)
            xR = [lowerX, upperX]
            yR = [lowerY, upperY]



            #Trying to create a plot with given fields, and if successful save it
            try:

                figure = interp(data_set, xIndex, yIndex, xLabel, yLabel, title, xR, yR, iKind)

                graph_image = 'interp.png'

                figure.savefig(os.path.join(graph_path, graph_image))

            except:

                #Returning error message on failure
                context={
                    'success': False,
                    'form': form,
                    'error_message': 'Something went wrong with creating the graph. Did you format your data properly?'
                }

                return render(request, template_name, context)

            #The final context dictionary with success being true. In this case, the error_message shouldn't pop up
            context = {
                'success': True,
                'form': form,
                'error_message': 'The graph should have been here, but something went wrong'
            }

    return render(request, template_name, context)









def package(request):

    template_name = 'Data_Science_Web_App/package.html'


    #Default rendering
    if request.method == "GET":
        context={
        'message' : ''
        }
        return render(request, template_name, context)

    if 'dl' in request.POST:
        try:
            csv_text = request.POST.get('csv_text')
            my_list = [num.strip() for num in csv_text.split(',')]
            response = HttpResponse(content_type = 'text/csv')
            response['Content-Disposition'] = 'attachment; filename = "export_data.csv"'

            writer = csv.writer(response, delimiter = ",")
            writer.writerow(my_list)

            return response

        except:
            context={
                'message': 'Something went wrong'
            }
            return render(request, template_name, context)

    elif 'package' in request.POST:
        key = generate_key(10)
        csv_text = request.POST.get('csv_text')
        my_list = [num.strip() for num in csv_text.split(',')]
        file_name = key + ".csv"
        with open(file_name,'w') as f:
            writer = csv.writer(f, delimiter = ",")
            writer.writerow(my_list)

        file_name = default_storage.save(file_name, open(file_name))
        temp = TemporaryFile(key = key, data = file_name)
        temp.save()
        context={
            'message': 'Saved! \n Here is your key: ' + key
        }
        return render(request, template_name, context)








def error_404(request, exception):
    template_name = 'Data_Science_Web_App/404.html'
    return render(request, template_name)


def error_500(request):
    template_name = 'Data_Science_Web_App/500.html'
    return render(request, template_name)

def error_403(request, exception):
    template_name = 'Data_Science_Web_App/403.html'
    return render(request, template_name)

def error_400(request, exception):
    template_name = 'Data_Science_Web_App/400.html'
    return render(request, template_name)
