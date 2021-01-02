from django import forms

class CardForm(forms.Form):
    # user = forms.CharField(label="Логин", max_length=100)
    title = forms.CharField(label="Заголовок", max_length=148)
    text = forms.CharField(label="Текст")
    color = forms.CharField(label='Цвет карточки', max_length=10)