from django import forms
from TELECOM.models import ourservices,imagemodel

class ourservicesform(forms.ModelForm):
    class Meta:
        model= ourservices
        fields= ('name', 'price', 'providercontact')



class imageuploadform(forms.ModelForm):
    class Meta:
        model = imagemodel
        fields = ['image','title','price']




