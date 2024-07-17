from django.shortcuts import render
from django.views.generic import ListView
from temoignage.models import Temoignage
from temoignage.form import TemoignageForm



# Create your views here.
def index(request):
    return render(request, 'index.html')


'''crud temoignage'''
class ListTemoignage(ListView):
    model = Temoignage
    context_object_name = 'temoignages'
    paginate_by = 10
    template_name = "temoignage/list.html"