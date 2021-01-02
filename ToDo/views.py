from django.shortcuts import render, redirect
from .forms import CardForm
from django.http import HttpResponse
from .models import Card


def home_page(request):
    if request.user.is_authenticated:
        cards = reversed(Card.objects.filter(user=request.user))
        return render(request, template_name='home/home.html', context={'cards': cards})
    return render(request, template_name='home/home.html', context={})


def create_card(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CardForm(request.POST)
            if form.is_valid():
                new_card = Card.objects.create(user=request.user,
                                               title=form.cleaned_data.get("title"),
                                               text=form.cleaned_data.get("text"),
                                               color=form.cleaned_data.get("color")
                                               )
                new_card.save()
    return redirect('/')

def edit_card(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CardForm(request.POST)
            card = Card.objects.filter(user=request.user, pk=id).first()
            if card and form.is_valid():
                card.title=form.cleaned_data.get("title")
                card.text=form.cleaned_data.get("text")
                card.color=form.cleaned_data.get("color")
                card.edited=True
                card.save()
    return redirect('/')


def delete_card(request, id):
    if request.user.is_authenticated:
        Card.objects.filter(user=request.user, pk=id).delete()
        return redirect('/')
    return render(request, template_name='home/home.html', context={})