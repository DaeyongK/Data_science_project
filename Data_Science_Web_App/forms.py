from django import forms
# from django.core import validators

class PlotChartForm(forms.Form):
    data_file = forms.FileField(label = 'CSV File')
    xIndex = forms.IntegerField(label = 'Index of X axis')
    yIndex = forms.IntegerField(label = 'Index of Y axis')
    xLabel = forms.CharField(required=False, label = 'Label for X axis')
    yLabel = forms.CharField(required=False, label = 'Label for Y axis')
    title = forms.CharField(required=False, label = 'Title of the graph')
    lowerX = forms.IntegerField(required=False, label = 'Minimum value of X axis')
    upperX = forms.IntegerField(required=False, label = 'Maximum value of X axis')
    lowerY = forms.IntegerField(required=False, label = 'Minimum value of Y axis')
    upperY = forms.IntegerField(required=False, label = 'Maximum value of Y axis')
    alphaVal = forms.IntegerField(required=False, label = 'Alpha Value')
