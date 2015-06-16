from django import forms
from django.contrib.auth.models import User
from .models import Rater
from .models import Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class RaterForm(forms.ModelForm):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = forms.ChoiceField(choices = GENDER_CHOICES, label="Gender", initial='', widget=forms.Select(), required=True)

    ONE = 1
    EIGHTTEEN = 18
    TWENTYFIVE = 25
    THIRTYFIVE = 35
    FORTYFIVE = 45
    FIFTY = 50
    FIFTYSIX = 56

    AGE_CHOICES = (
        (ONE, "Under 18"),
        (EIGHTTEEN, "18-24"),
        (TWENTYFIVE, "25-34"),
        (THIRTYFIVE, "35-44"),
        (FORTYFIVE, "45-49"),
        (FIFTY, "50-55"),
        (FIFTYSIX, "56+"),
    )

    age = forms.ChoiceField(choices=AGE_CHOICES, label="Age", initial='', widget=forms.Select(), required=True)

    OTHER = 0
    ACADEMIC = 1
    ARTIST = 2
    ADMIN = 3
    COLLEGE = 4
    SERVICE = 5
    DOCTOR = 6
    EXEC = 7
    FARMER = 8
    HOMEMAKER = 9
    STUDENT = 10
    LAWYER = 11
    PROGRAMMER = 12
    RETIRED = 13
    SALES = 14
    SCEINTIST = 15
    SELF = 16
    TECH = 17
    TRADE = 18
    UNEMPLOYED = 19
    WRITER = 20

    JOB_CHOICE = (
       (OTHER, "other"),
       (ACADEMIC, "academic/educator"),
       (ARTIST, "artist"),
       (ADMIN, "clerical/admin"),
       (COLLEGE, "college/grad student"),
       (SERVICE, "customer service"),
       (DOCTOR, "doctor/health care"),
       (EXEC, "executive/managerial"),
       (FARMER, "farmer"),
       (HOMEMAKER, "homemaker"),
       (STUDENT, "K-12 student"),
       (LAWYER, "lawyer"),
       (PROGRAMMER, "programmer"),
       (RETIRED, "retired"),
       (SALES, "sales/marketing"),
       (SCEINTIST, "scientist"),
       (SELF, "self-employed"),
       (TECH, "technician/engineer"),
       (TRADE, "tradesman/craftsman"),
       (UNEMPLOYED, "unemployed"),
       (WRITER, "writer"))
    job = forms.ChoiceField(choices=JOB_CHOICE, label="Job", initial='', widget=forms.Select(), required=True)

    postal_code = forms.CharField(max_length=10)

    class Meta:
        model = Rater
        fields = ('job', 'age', 'gender', "postal_code")


class RatingForm(forms.ModelForm):

 # text_rating = forms.CharField(max_length=255)

 class Meta:
    model = Rating
    fields = ('rating',)