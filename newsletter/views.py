from django.shortcuts import render

from .forms import ContactForm, SignUpForm


def home(request):
    title = 'Welcome'

    if request.POST == 'POST':
        print(request.POST)
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance)
        instance.save()


    context = {
        "form": form,
        'title': title,
    }

    return render(request, "newsletter/signup.html", context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    context = {
        "form": form,
    }


    return render(request, "newsletter/contact.html", context)