from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, TemplateView

from .models import Attraction, AttractionStatus
from .forms import AttractionFrom, AttractionAddressForm


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


# class AttractionCreateView(LoginRequiredMixin, CreateView):
#     form_class = AttractionFrom
#     login_url = '/login/'
#     template_name = 'attractions/create_attraction_form.html'
#     success_url = '/attractions/'
#
#
#     def form_valid(self, form):
#         print(form)
#         instance = form.save(commit=False)
#         instance.owner = self.request.user
#
#         return super(AttractionCreateView, self).form_valid(form)


@login_required(login_url='/login')
def attraction_createviews(request):
    attraction_form = AttractionFrom(request.POST or None)
    addres_form = AttractionAddressForm(request.POST or None)

    if attraction_form.is_valid() and addres_form.is_valid():

        attraction = attraction_form.save(commit=False)
        attractions = Attraction.objects.filter((Q(name__iexact=attraction.name) |
                                                Q(name__icontains=attraction.name)) &
                                                (Q(category__iexact=attraction.category) |
                                                Q(category__icontains=attraction.category))
                                                )
        addres = addres_form.save(commit=False)

        attraction.owner = request.user
        attraction.save()

        addres.attraction = attraction

        addres.save()

        if len(attractions) > 1:
            dublicate = True
        else:
            dublicate = False

        AttractionStatus.objects.create(attraction=attraction, is_active=False,
                                        is_verified=False, points=0, is_dublicated = dublicate)

        return HttpResponseRedirect(reverse('attractions:attractions_list'))


    template_name = 'attractions/create_attraction_form.html'
    context = {"attraction_form": attraction_form,
               "addres_form": addres_form}

    return render(request, template_name, context)