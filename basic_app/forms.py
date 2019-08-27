from django import forms
from .models import Invoice_Data

class PostForm(forms.ModelForm):
    class Meta:
        model = Invoice_Data
        fields = ['description','hsn','pack','batch','exp_date','qty','free','mrp','rate','gst','amount']
