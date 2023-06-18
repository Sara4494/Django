
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ModelForm, DateField, widgets
from app.models import *
'''
class SaveUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        '''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	 
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class NewProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields =("image","phone_number","phone_number2")
		widgets = {
			'image':forms.FileInput(attrs={'class':'form-control'}),
		}
 
class NewTrendy_ProductsForm(forms.ModelForm):

	class Meta:
		model = Trendy_Products
		fields =('name','photo')
		 