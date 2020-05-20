from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    OPTIONS1 = (
        ('estudiante','Estudiante'),
        ('profesor','Profesor'),
        )
    role = forms.ChoiceField(label = ("Seleccione Rol/Cargo"), required=True, choices=OPTIONS1)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        
        fields = ('email', 'username','first_name','last_name','role',)
        
        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Primer Apellido',
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
