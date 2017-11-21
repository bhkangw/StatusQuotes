from django.shortcuts import render, redirect
from ..login.models import User
from .models import Quote
from datetime import datetime
from django.contrib import messages
import operator


def index(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        "all": Quote.objects.restofquotes(request.session['user_id']),
        "fav": User.objects.get(id=request.session['user_id']).favorite_quotes.all(),
    }
    return render(request, 'quotes/index.html', context)


def add(request):
    response = Quote.objects.quote_validator(request.POST,request.session['user_id'])
    if response['status'] == True:
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.create(
            quote=request.POST['quote'],
            author=request.POST['author'],
            user=user,
        )
        return redirect('/quotes')
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/quotes')
    return redirect('/quotes')


def addfav(request, id):
    response = Quote.objects.addfav(id)
    if response['status'] == True:
        this_user = User.objects.get(id=request.session['user_id'])
        this_quote = Quote.objects.get(id=id)
        this_user.favorite_quotes.add(this_quote)
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/quotes')
    return redirect('/quotes')


def removefav(request, id):
    response = Quote.objects.removefav(id)
    if response['status'] == True:
        this_user = User.objects.get(id=request.session['user_id'])
        this_quote = this_user.favorite_quotes.all().get(id=id)
        this_user.favorite_quotes.remove(this_quote)
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/quotes')
    return redirect('/quotes')


def logout(request):
    request.session.clear()
    return redirect('/')

# def addfav(request, id):
#     # user = User.objects.get(id=request.session['user_id'])
#     # print user.id
#     # quote = Quote.objects.get(id=id)
#     # print quote
#     # return redirect('/quotes')