from django.forms import ModelForm
from .models import Day


class TableForm(ModelForm):
    class Meta:
        model = Day
        fields = '__all__'
