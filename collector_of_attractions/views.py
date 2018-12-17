from django.shortcuts import render, HttpResponseRedirect


from .forms import AttractionCreateForm


def attraction_createview(request):
    form = AttractionCreateForm(request.POST or None)
    errors = None

    if form.is_valid():
        obj = AttractionCreateForm.objects.create(
            name = form.cleaned_data.get('name'),
            category = form.cleaned_data.get('category'),
            short_description= form.cleaned_data.get('short_description'),
            long_description= form.cleaned_data.get('long_description')
        )
        return HttpResponseRedirect("/")

    if form.errors:
        errors = form.errors

    template_name = 'collector_of_attractions/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)