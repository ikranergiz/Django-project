from django import forms
from .models import Hotel
 
 
class HotelForm(forms.ModelForm):
 
    class Meta:
        model = Hotel
        fields = ['hotel_Main_Img']