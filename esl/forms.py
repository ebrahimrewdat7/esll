from logging import PlaceHolder
from tkinter import Widget
from turtle import width
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms import Form

from esl.models import VideoLecture


class DateInput(forms.DateInput):
    input_type = "date"


class AddAdminForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))


class SignupLearnerForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput)
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput)
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput)
    username = forms.CharField(label="Username", max_length=10, widget=forms.TextInput)
    password1 = forms.CharField(label="Password", max_length=12,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Retype Password", max_length=12,
                                widget=forms.PasswordInput)

    


class SignupInstructorForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput)
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput)
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput)


    username = forms.CharField(label="Username", max_length=10, widget=forms.TextInput)
   
    phoneNo = PhoneNumberField(label="Phone Number", widget=PhoneNumberPrefixWidget(initial='ET')
                               )
    document = forms.FileField(label="Document",widget=forms.ClearableFileInput)
    id_pic = forms.ImageField(label="ID Image", widget=forms.ClearableFileInput)
    description = forms.CharField(label="Description", max_length=255, widget=forms.Textarea)
    password1 = forms.CharField(label="Password", max_length=12,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Retype Password", max_length=12,
                                widget=forms.PasswordInput)


Basic_Type_CHOICES = (
   
    ("English", "English Alphabet"),
    ("Amharic", "Amharic Alphabet"),
    ("Number", "Numbers"),
    ("Week", "Weeks"),
    ("Day", "Days"),
    ("Body", "Body Parts"),
    ("Family", "Family"),
    ("Maths", "Maths"),
     
)

Intermediate_Type_CHOICES = (
   
    ("Cloths", "Cloths"),
    ("Food", "Food"),
    ("Animals", "Animals"),
    ("Natures", "Natures"),
    ("Color", "Color"),
    ("Fruit", "Fruit"),
    ("Vegetable", "Vegetable"),
    ("Names", "Names"),
     
)

Advanced_Type_CHOICES = (
   
    ("Spiritual", "Spiritual"),
    ("Question", "Question"),


     
)

class AddBeginnerSign(forms.Form):
    signImage = forms.ImageField(label="Sign Image", max_length=50,
                                 widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    type = forms.ChoiceField(label="Type", choices=Basic_Type_CHOICES,
                             widget=forms.Select(attrs={"class": "form-select"}))
    textForSign = forms.CharField(label="Text Description", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))

class AddIntermediateSign(forms.Form):
    signImage = forms.ImageField(label="Sign Image", max_length=50,
                                 widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    type = forms.ChoiceField(label="Type", choices=Intermediate_Type_CHOICES,
                             widget=forms.Select(attrs={"class": "form-select"}))
    textForSign = forms.CharField(label="Text Description", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))

class AddAdvancedSign(forms.Form):
    signImage = forms.ImageField(label="Sign Image", max_length=50,
                                 widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    type = forms.ChoiceField(label="Type", choices=Advanced_Type_CHOICES,
                             widget=forms.Select(attrs={"class": "form-select"}))
    textForSign = forms.CharField(label="Text Description", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))

class AddBeginnerVideoLecture(forms.ModelForm):
    type = forms.ChoiceField(label="Type", choices=Basic_Type_CHOICES,
                            widget=forms.Select(attrs={"class": "form-select"}))
    class Meta:
        model=VideoLecture
        fields=('video','caption',)
class AddIntermediateVideoLecture(forms.ModelForm):
    type = forms.ChoiceField(label="Type", choices=Intermediate_Type_CHOICES,
                            widget=forms.Select(attrs={"class": "form-select"}))
    class Meta:
        model=VideoLecture
        fields=('video','caption',)
class AddAdvancedVideoLecture(forms.ModelForm):
    type = forms.ChoiceField(label="Type", choices=Advanced_Type_CHOICES,
                            widget=forms.Select(attrs={"class": "form-select"}))
    class Meta:
        model=VideoLecture
        fields=('video','caption',)