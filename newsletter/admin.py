from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'timestamp', 'updated']
    # connection with forms.py
    form = SignUpForm

    # Connection with models.py
    #
    # class Meta:
    #     model = SignUp
    #     ordering = ['-timestamp']


admin.site.register(SignUp, SignUpAdmin)
