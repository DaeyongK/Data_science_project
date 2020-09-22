from django.shortcuts import render
from django.views.generic import TemplateView
from Data_Science_Web_App.algorithms.average import average, median, mode, strWSpace
from Data_Science_Web_App.algorithms.xyplot import xyplot
from Data_Science_Web_App.algorithms.histo import histo
from . import forms
import os
import pandas
import mpld3

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
def get_average(request):

    template_name = 'Data_Science_Web_App/average.html'

    #Default rendering
    if request.method == "GET":
        context={
            'num': 'Please upload a CSV file',
            'left': 'Please upload a CSV file',
            'mid': 'Please upload a CSV file',
            'right': 'Please upload a CSV file',
            'mode': 'Please upload a CSV file'
        }
        return render(request, template_name, context)

    #Checking if user filled out both areas
    try:
        csv_file = request.FILES['file_name']
        csv_text = request.POST.get('csv_text')
        #But if csv_text is empty which means that the textarea was left alone,
        if csv_text == "":

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

        #This will run only if the user pressed upload without providing any data
        if csv_text == "":
            context={
                'num': 'Please provide an input'
            }
            return render(request, template_name, context)

        data_set = csv_text

    #Running the algorithms on the data_set
    try:
        avgNum = average(data_set)
        left,mid,right = median(data_set)
        if mode(data_set) == None:
            modeNum = "There was no mode in the given data"
        else:
            modeNum = " ".join(list(map(strWSpace, mode(data_set))))[:-2]

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
        'mode': modeNum
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
