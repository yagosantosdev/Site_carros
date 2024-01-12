from django.http import HttpResponse
from django.shortcuts import redirect, render
from cars.forms import CarModelForm
from cars.models import Car


def cars_view(request):
   cars = Car.objects.all().order_by('model')
   search = request.GET.get('search')


   if search:      
      cars = Car.objects.filter(model__icontains= search )


   return render(
        request,
        'cars.html', 
        {'cars': cars}
        )



def  new_car_view(request):
  if request.method == 'POST':
     new_car_form = CarModelForm(request.POST , request.FILES) # para receber o metodo post e recebr aquivos que seria as imagens 
     if new_car_form.is_valid(): # validação para saber se os dados são validos
        new_car_form.save() # o save foi configurado com as tabelas no arquivo forms.py
        return redirect('cars_list') # o nome ja diz redireciona para a lista de carros 
     
  else:
      new_car_form = CarModelForm()
  return render(request,'new_car.html' , {'new_car_form': new_car_form})