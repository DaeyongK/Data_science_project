from django import forms
# from django.core import validators

class PlotChartForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    xIndex = forms.IntegerField(label = 'Index of X axis')
    yIndex = forms.IntegerField(label = 'Index of Y axis')
    xLabel = forms.CharField(required=False, label = 'Label for X axis')
    yLabel = forms.CharField(required=False, label = 'Label for Y axis')
    title = forms.CharField(required=False, label = 'Title of the graph')
    lowerX = forms.DecimalField(required=False, label = 'Minimum value of X axis')
    upperX = forms.DecimalField(required=False, label = 'Maximum value of X axis')
    lowerY = forms.DecimalField(required=False, label = 'Minimum value of Y axis')
    upperY = forms.DecimalField(required=False, label = 'Maximum value of Y axis')
    alphaVal = forms.DecimalField(required=False, label = 'Alpha Value')


class HistoForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    colN = forms.IntegerField(label = 'Column Number')
    xLabel = forms.CharField(required=False, label = 'Label for X axis')
    yLabel = forms.CharField(required=False, label = 'Label for Y axis')
    title = forms.CharField(required=False, label = 'Title of the graph')
    lowerX = forms.DecimalField(required=False, label = 'Minimum value of X axis')
    upperX = forms.DecimalField(required=False, label = 'Maximum value of X axis')
    lowerY = forms.DecimalField(required=False, label = 'Minimum value of Y axis')
    upperY = forms.DecimalField(required=False, label = 'Maximum value of Y axis')
    hStyle = forms.ChoiceField(widget=forms.RadioSelect, choices = [('bar', 'Bar'),('barstacked','Bar Stacked'), ('step', 'Step'), ('stepfilled', 'Step Filled')], label = 'Which histogram style would you like?')
    binS = forms.IntegerField(required=False, label = 'Size of bins')
    densYes = forms.ChoiceField(widget=forms.RadioSelect, choices=[(True, 'Yes'), (False, 'No')], label = 'Do you want a density function?')


class InterpolationForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    xIndex = forms.IntegerField(label = 'Index of X axis')
    yIndex = forms.IntegerField(label = 'Index of Y axis')
    xLabel = forms.CharField(required=False, label = 'Label for X axis')
    yLabel = forms.CharField(required=False, label = 'Label for Y axis')
    title = forms.CharField(required=False, label = 'Title of the graph')
    lowerX = forms.DecimalField(required=False, label = 'Minimum value of X axis')
    upperX = forms.DecimalField(required=False, label = 'Maximum value of X axis')
    lowerY = forms.DecimalField(required=False, label = 'Minimum value of Y axis')
    upperY = forms.DecimalField(required=False, label = 'Maximum value of Y axis')
    iKind = forms.CharField(required=False, label = 'Kind of Interpolation')

class CurveFitterForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    xIndex = forms.IntegerField(label = 'Index of X axis')
    yIndex = forms.IntegerField(label = 'Index of Y axis')
    xLabel = forms.CharField(required=False, label = 'Label for X axis')
    yLabel = forms.CharField(required=False, label = 'Label for Y axis')
    title = forms.CharField(required=False, label = 'Title of the graph')
    lowerX = forms.DecimalField(required=False, label = 'Minimum value of X axis')
    upperX = forms.DecimalField(required=False, label = 'Maximum value of X axis')
    lowerY = forms.DecimalField(required=False, label = 'Minimum value of Y axis')
    upperY = forms.DecimalField(required=False, label = 'Maximum value of Y axis')
    fit_func = forms.CharField(required=False, label = 'Fit Function')
    y_func = forms.CharField(required=False, label = 'Y Function')

class LogForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    colN = forms.IntegerField(label = 'Column Number')
    negative = forms.ChoiceField(widget=forms.RadioSelect, choices=[(True, 'Yes'), (False, 'No')], label = 'Do you want your values to be non negative?')
    package = forms.ChoiceField(widget=forms.RadioSelect, choices=[(True, 'Package'), (False, 'Download')], label = 'Do you want to package or download your data?')

class CustomForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    code = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':100, 'style': 'width:100%;'}), label = 'Code')
    package = forms.ChoiceField(widget=forms.RadioSelect, choices=[(True, 'Package'), (False, 'Download')], label = 'Do you want to package or download your data?')

class VarForm(forms.Form):
    key = forms.CharField(required=False, label = 'Key')
    data_file = forms.FileField(required=False, label = 'CSV File')
    rc = forms.ChoiceField(widget=forms.RadioSelect, choices=[(True, 'Row'), (False, 'Column')], label = 'Row or Column?')
    num = forms.IntegerField(label = 'Row/Column Number')

class CustomVisualForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
    key = forms.CharField(required=False, label = 'Key')
    code = forms.CharField(widget=forms.Textarea(attrs={'rows':20, 'cols':100, 'style': 'width:100%;'}), label = 'Code')

class UploadForm(forms.Form):
    data_file = forms.FileField(required=False, label = 'CSV File')
