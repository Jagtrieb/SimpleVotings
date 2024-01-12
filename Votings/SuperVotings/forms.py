from django import forms


class RadioForm(forms.Form):
    names = []
    variants = []
    for i in range(len(names)):
        variants.append(forms.RadioSelect)
