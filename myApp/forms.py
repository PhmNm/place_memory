from django.forms import ModelForm
from .models import *

class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['place_name', 'comments', 'longitude', 'latitude']
        