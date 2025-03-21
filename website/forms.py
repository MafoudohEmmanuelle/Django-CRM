from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Records

class SignUpForm(UserCreationForm):	
   email= forms.EmailField( label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
   first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
   last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

   class Meta:
      model=User
      fields=('username','first_name','last_name','email','password1','password2')

   def __init__(self, *args, **kwargs ):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class']='form-control'
      self.fields['username'].widget.attrs['placeholder']='Username'         
      self.fields['username'].label=''

      self.fields['password1'].widget.attrs['class']='form-control'
      self.fields['password1'].widget.attrs['placeholder']='Password'         
      self.fields['password1'].label=''

      self.fields['password2'].widget.attrs['class']='form-control'        
      self.fields['password2'].widget.attrs['placeholder']='Confirm Password'        
      self.fields['password2'].label=''



#Create add record form
class AddRecordForm(forms.ModelForm):
   first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="", max_length=100)
   last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="", max_length=100)
   email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email ", "class":"form-control"}), label="", max_length=50)
   phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="",max_length=50)
   address= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="",max_length=50)
   city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="",max_length=50)
   state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="",max_length=50)
   zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="",max_length=50)

   class Meta:
      model = Records
      exclude = ("user",)