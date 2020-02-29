from django.shortcuts import render
from django.views import generic
from .models import Location,Property

# Create your views here.
class IndexView(generic.ListView):
    template_name='homesapp1/index.html'

    def get_queryset(self):
        return Location.objects.all()


class LocationView(generic.DetailView):
    model =  Location
    template_name = 'homesapp1//locationview.html'

class PropertyDetails(generic.DetailView):
    model = Property
    template_name = 'homesapp1/propertyview.html'