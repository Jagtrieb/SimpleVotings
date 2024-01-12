from django import forms


class RadioForm(forms.Form):
    varinats = ('putin', 'Putin'), ('trump', 'Trump'), ('xin', "Xin Jin Ping")
    candidates = forms.ChoiceField(choices=varinats, widget=forms.RadioSelect)
