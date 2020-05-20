from django import forms
from classroom.models import Grades
from django.core.validators import MaxValueValidator, MinValueValidator


class GradesForm(forms.ModelForm):
    first_trimester = forms.FloatField(min_value=0.0, max_value=10.0, label="1er Parcial",
        widget=forms.NumberInput(attrs={'id': 'first_trimester', 'step': "0.1"})) 
    second_trimester = forms.FloatField(min_value=0.0, max_value=10.0, label="2do Parcial",
        widget=forms.NumberInput(attrs={'id': 'second_trimester', 'step': "0.1"})) 
    third_trimester = forms.FloatField(min_value=0.0, max_value=10.0, label="3er Parcial",
        widget=forms.NumberInput(attrs={'id': 'third_trimester', 'step': "0.1"})) 
    final_exam = forms.FloatField(min_value=0.0, max_value=10.0, label="Examen Final",
        widget=forms.NumberInput(attrs={'id': 'final_exam', 'step': "0.1"})) 
    class Meta:
        model = Grades
        fields = ('first_trimester','second_trimester','third_trimester','final_exam')
