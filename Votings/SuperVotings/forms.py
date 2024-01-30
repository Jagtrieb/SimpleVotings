from django import forms


class RadioForm(forms.Form):
    varinats = ('putin', 'Putin'), ('trump', 'Trump'), ('xin', "Xin Jin Ping")
    candidates = forms.ChoiceField(choices=varinats, widget=forms.RadioSelect)

class AddSnippetForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        label='Код',
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'style': 'height:500px'
            }
        )
    )