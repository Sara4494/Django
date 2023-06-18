from django import forms
from .models import *

class ProductFormSimple(forms.Form):
    name = forms.CharField(max_length=120)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = "__all__"
        fields = ['name','price','magmo3a']
        
class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        #fields = "__all__"
        fields = ['name','count','active']
        
class Elmamo3aForm(forms.ModelForm):
     class Meta:
        model = Elmagmo3a
        fields = "__all__"
        #fields = ['name','price','magmo3a','count']