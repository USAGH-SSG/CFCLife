from django import forms

from .models import TaxiParty, Route, Location

class TaxiPartyForm(forms.ModelForm):
    class Meta:
        model = TaxiParty
        fields = [
            'date',
            'time',
            'route',
            'rider',
        ]

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'name'
        ]

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = [
            'origin',
            'destination'
        ]
    
    def is_valid(self) -> bool:
        if self['origin'] == self['destination']:
            raise forms.ValidationError("Origin and destination cannot be identical")
        return super().is_valid()