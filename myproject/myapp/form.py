from django import forms
from myapp.models import empl,Tech,crud
class employee(forms.ModelForm):
    class Meta:
        model=empl
        fields='__all__'


class stdform(forms.Form): #django form~
    firstname=forms.CharField(label="enter first name",max_length=50)
    lastname=forms.CharField(label="enter last name",max_length=5)

class file(forms.ModelForm):
    class Meta:
        mod=Tech
        fields='__all__'


class curdd(forms.ModelForm):
    class Meta:
        model=crud
        fields='__all__'