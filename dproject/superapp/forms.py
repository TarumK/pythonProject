from django import forms

class UserForm(forms.Form):
    some_tuple = (1, 2)
    name = forms.CharField(label='Имя', initial='Наберите имя')
    age = forms.IntegerField(label='Возраст')
    obr = forms.BooleanField(label='Выcшее образование')
    town = forms.ChoiceField(choices=(('1', 'Москва'), ('2', 'Али-Бердуковский')))
