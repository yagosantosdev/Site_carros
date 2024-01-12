from django import forms 
from cars.models import Car 



#formulario em django super simples 
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car # aqui falamos que o formulario é referente a tabela car 
        fields = '__all__' # seleciona todos os campos do model do car 
