#Here are some instructions for creating your own algorithms, forms, views, and HTML pages


#Follow these steps for views that take in csv files and outputs a graph using an algorithm, like plotting

# 1. Create your algorithm in Data_Science_Project/Data_Science_Web_App/algorithms/name_of_algorithm.py
#   a. Make sure to take in a file as a parameter, and you can include other parameters for customization if you want to
#   b. Have default values for variables, because users will not be required to fill in all fields
#   c. Return a pyplot figure at the end of your algorithm

# 2. Create a custom Django Form in Data_Science_Project/Data_Science_Web_App/forms.py
#   a. Refer to the Django Form Example at line 37 to create a form properly

# 3. Create your own HTML page for your algorithm in Data_Science_Project/Data_Science_Web_App/templates/Data_Science_Web_App/name_of_template.html
#   a. Refer to madlibs.html, line 1, to create an HTML page properly

# 4. Create your custom function based view in Data_Science_Project/Data_Science_Web_App/views.py
#   a. Refer to the Django View Example at line 60 to create a view properly

# 5. Edit Data_Science_Project/Data_Science_Web_App/urls.py (Be wary as there are two urls.py in this project; use the one within Data_Science_Web_App)
#   a. Refer to the Django URL Example at line 140 to create a path properly

# 6. Add in a shortcut to your algorithm in Data_Science_Project/Data_Science_Web_App/templates/Data_Science_Web_App/base.html
#   a. Refer to madlibs.html, line 35, to link your algorithm properly

# 7. Test out your algorithm by running a local server
#   a. Change directories in your terminal until you are in the directory with manage.py in it
#   b. Make sure you're using a virtual environment with all necessary packages, or create a virtual environment with all the packages in requirements.txt
#   c. Activate your virtual environment
#   d. Type in "python3 manage.py runserver" in your terminal
#   e. Copy the link that the terminal outputs and put it into your browser
#   f. Test your algorithm out with an appropriate csv file within the tests directory




# Django Form Example
class NameOfForm(forms.Form):
    # Here are some options for Form fields
    # Once again, the data_file variable is necessary
    data_file = forms.FileField(label = 'CSV File')
    # Option to take in Floats or Decimals (It is recommended that you use decimals whenever it is possible, as it offers more flexibility)
    decimal_field_name = forms.DecimalField(label = 'name_of_field')
    # Option to take in Integers
    integer_field_name = forms.IntegerField(label = 'name_of_field')
    # Option to take in characters or text
    # Note the optional "required" parameter; set this to False if the user does not need to provide a value for this field
    character_field_name = forms.CharField(required=False, label = 'name_of_field')
    # Option to provide user with choices
    # Note the Django widgets used in some fields; to find out more about widgets, view the documentation at https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#built-in-widgets
    # When programming choices in the format of ('option_1', 'option_1'), the first 'option_1' is what the field variable will contain if the user selects that option
    # The second 'option_1' is what the user will see on the website, and of course, the label can be anything that's appropriate for the situation
    choice_field_name = forms.ChoiceField(widget=forms.RadioSelect, choices = [('option_1', 'option_1'),('option_2','option_2')], label = 'Which option would you like to select?')






# Django View Example
def name_of_view(request):

    #HTML template that the view is connected to
    template_name = 'Data_Science_Web_App/name_of_template.html'
    #Name of custom Django Form for your algorithm
    form = forms.NameOfForm()
    #This is the context dictionary that can interact with your HTML template, you don't need to edit this
    context={
        'success': False,
        'form': form,
        'error_message': 'Please fill out the required fields!'
    }


    if request.method == 'POST':

        form = forms.NameOfForm(request.POST, request.FILES)

        if form.is_valid():

            # Leave this line alone, since all forms will have a data_file field
            data_file = form.cleaned_data['data_file']

            # Write a line for every field other than data_file in your custom Django Form
            # For example, if the field in your form was: title = forms.CharField(required=False, label = 'Title of the graph')
            # your line of code would look like: title = form.cleaned_data['title']
            # note that you can set the variable name to anything, but it is recommended that you use the same name as the field in the form
            form_field = form.cleaned_data['form_field']
            form_field_2 = form.cleaned_data['form_field_2']

            if not data_file.name.endswith('.csv'):

                context={
                    'success': False,
                    'form': form,
                    'error_message': 'The input type was invalid; did you make sure you used a CSV file?'
                }

                return render(request, template_name, context)


            #Reading data_file with pd, so that data_set is now a pd dataframe
            data_set = pd.read_csv(data_file)

            try:

                # First, import your algorithm into views.py by calling: from Data_Science_Web_App.algorithms.name_of_algorithm import name_of_algorithm
                # Then, call the function with its appropriate parameters, then set it equal to a figure variable
                figure = name_of_algorithm(data_set, form_field, form_field_2)

                # Give your graph a unique name, different from other names in Data_Science_Project/media/graphs
                graph_image = 'name_of_graph.png'

                #Don't worry about the graph_path variable, it is defined at the top of views.py
                figure.savefig(os.path.join(graph_path, graph_image))

            except:

                context={
                    'success': False,
                    'form': form,
                    'error_message': 'Something went wrong with creating the graph. Did you format your data properly?'
                }

                return render(request, template_name, context)

            context = {
                'success': True,
                'form': form,
                'error_message': 'The graph should have been here, but something went wrong'
            }

    return render(request, template_name, context)






# Django URL Example
# Add this line of code to the end of the list in urls.py
path('url_path_name/', views.name_of_view, name='name_of_view'),
# The 'url_path_name/' is the extension on the base url of the website that will appear when the user navigates to your page
# views.name_of_view refers to the name of the function based view you created in views.py
# The final 'name_of_view' is the name you will use to connect the view to a shortcut in an HTML page
