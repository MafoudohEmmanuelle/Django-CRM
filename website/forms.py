from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email= forms.EmailField( label="", widget=forms.TestInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	first_name=forms.CharField(label="",max_length=100,widget=forms.TestInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name=forms.CHarField(label="",max_length=100,widget=forms.TestInput(attrs={'class':'form-control','placeholder':'First Name'}))
