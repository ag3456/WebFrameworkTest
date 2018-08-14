from django import forms



class InputForm(forms.Form):
    MYCHOICES = (
        ('1', 'Poker Flat ISR'),
        ('2', 'Millstone Hill')
    )
    location=forms.ChoiceField(choices=MYCHOICES)
    fromdate = forms.DateField()
    todate=forms.DateField()