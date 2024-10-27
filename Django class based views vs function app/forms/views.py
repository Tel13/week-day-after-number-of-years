from tempfile import template

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import InputForm
from .models import InputFromsModel
from django.urls import reverse
from django.template import loader

# Create your views here.
def success():
    return HttpResponse("<h1>Success data</h1>")

def home_view(request):
    form = InputForm()

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            form = InputForm()

    context = {'form' : form}
    return render(request, "forms/home.html", context)

def extract_data_from_forms(request):
    dataform = InputFromsModel.objects.all()
    context = {'dataform' : dataform }
    return render(request, 'forms/data-forms.html', context)

def delete_data_from_db(request, id):
    dataFromDb = InputFromsModel.objects.get(id=id)
    dataFromDb.delete()
    return HttpResponseRedirect(reverse('home'))

def update_data_from_db(request, id):
    dataFromDb = InputFromsModel.objects.get(id=id)
    template = loader.get_template('forms/update.html')
    context = {'dataFromDb' : dataFromDb}
    return HttpResponse(template.render(context, request))

def update_record(request, id):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    rollNumber = request.POST['roll_number']
    password = request.POST['password']
    dataFromDb = InputFromsModel.objects.get(id=id)
    dataFromDb.first_name = firstName
    dataFromDb.last_name = lastName
    dataFromDb.roll_number = rollNumber
    dataFromDb.password = password
    dataFromDb.save()
    return HttpResponseRedirect(reverse('display-data'))
