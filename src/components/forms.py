from django import forms

from .models import Component

class ComponentForm(forms.ModelForm):
    CompName    = forms.CharField(
                label="",
                widget=forms.TextInput(
                    attrs={
                        'placeholder': 'Name'
                    }
                )
            )
    
    Company     = forms.CharField(
                label="",
                widget=forms.TextInput(
                    attrs={
                        'placeholder': 'Company'
                    }
                )
            )

    Description = forms.CharField(
                label="",
                required=False, 
                widget=forms.Textarea(
                    attrs={
                        'rows': 5,
                        'cols': 26,
                        'placeholder': 'Description'
                    }
                )
            )

    AvgPrice    = forms.DecimalField(
                label="", 
                min_value=0, 
                initial=0
            )
    class Meta:
        model = Component
        fields = [
            'CompName',
            'Company',
            'Description',
            'AvgPrice'
        ]


class RawComponentForm(forms.Form):
    CompName    = forms.CharField(
                    label="",
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Name'
                        }
                    )
                )
    Company     = forms.CharField(
                    label="",
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Company'
                        }
                    )
    )
    Description = forms.CharField(
                    label="",
                    required=False, 
                    widget=forms.Textarea(
                        attrs={
                            'rows': 5,
                            'cols': 30,
                            'placeholder': 'Description'
                        }
                    )
                )
    AvgPrice    = forms.DecimalField(label="", 
                    min_value=0, 
                    initial=0
                )