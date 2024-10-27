from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import GeeksModel
from .forms import GeeksForm
from django.urls import reverse_lazy, reverse


# Create your views here.
class MyView(View):
    def get(self, request):
        #return HttpResponse('templates/index.html')
        return render(request, "index.html")

class GeeksCreateView(CreateView):
    model = GeeksModel
    template_name = "create.html"
    #fields = ['title', 'description']
    fields = '__all__'
    success_url = reverse_lazy('index')

class GeeksListView(ListView):
    model = GeeksModel
    template_name = "listview.html"
    fields = ('title','description')

class GeeksDetailView(DetailView):
    model = GeeksModel
    template_name = "detail_view.html"

class GeeksUpdateView(UpdateView):
    model = GeeksModel
    template_name = "update.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('listview')

class GeeksDeleteView(DeleteView):
    model = GeeksModel
    template_name = "delete.html"
    success_url = reverse_lazy('listview')
