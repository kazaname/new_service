from django.db.models import Q
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView, CreateView

from .models import Attraction
from .forms import AttractionCreateModelFrom


def attraction_createview(request):
    form = AttractionCreateModelFrom(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/attractions/")

    if form.errors:
        errors = form.errors
    tempalte_name = 'collector_of_attractions/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, tempalte_name, context)

class HomeView(TemplateView):
    template_name = 'base.html'


class AttractionDetailView(DetailView):

    model = Attraction

    def get_object(self, queryset=None, *args, **kwargs):
        object = super().get_object(*args, **kwargs)
        return object


class AttractionListView(ListView):

    def get_queryset(self):
        queryset = Attraction.objects.all()

        return queryset


class CategoryListView(ListView):

    def get_queryset(self):
        cat = self.kwargs.get("cat")
        if cat:
            queryset = Attraction.objects.filter(
                Q(category__iexact=cat) |
                Q(category__icontains=cat)
            )
        else:
            queryset = Attraction.objects.none()

        return queryset


class AttractionCreateView(CreateView):
    form_class = AttractionCreateModelFrom
    template_name = 'collector_of_attractions/form.html'
    success_url = '/attractions/'