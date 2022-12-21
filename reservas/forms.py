from django import forms
from django.forms import ModelForm 
from .models import Vehiculo,Reserva_Inicial1,Reserva_Inicial2,Reserva_Final1,Reserva_Final2
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

class RegisterUserForm(UserCreationForm):

    class_attr_inputs = 'form-control input_for_form mt-2'
    
    username = UsernameField(label=("Usuario*"),
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingrese usuario'}),
                help_text=(""))

    first_name = forms.CharField(label=("Nombre*"),
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresa tu nombre'}),
                help_text=(""))
    
    last_name = forms.CharField(label=("Apellido*"),
                widget=forms.TextInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresa tu nombre'}),
                help_text=(""))

    email = forms.CharField(label=("Correo electrónico*"),
                widget=forms.EmailInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresa tu correo electrónico'}),
                help_text=(""))

    password1 = forms.CharField(label=("Contraseña*"),
                widget=forms.PasswordInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresa tu correo electrónico'}),
                help_text=(""))
    
    password2 = forms.CharField(label=("Confirme Contraseña*"),
                widget=forms.PasswordInput(attrs={'class':class_attr_inputs,'placeholder':'Ingresa tu correo electrónico'}),
                help_text=(""))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']



class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class Reserva_Inicial1Form(ModelForm):

    class Meta:
        model = Reserva_Inicial1
        fields = '__all__'
        
class Reserva_Inicial2Form(ModelForm):

    class Meta:
        model = Reserva_Inicial2
        fields = '__all__'
        
class Reserva_Final1Form(ModelForm):

    class Meta:
        model = Reserva_Final1
        fields = '__all__'

class Reserva_Final2Form(ModelForm):

    class Meta:
        model = Reserva_Final2
        fields = '__all__'
        

