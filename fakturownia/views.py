# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import collections
from django.shortcuts import render, get_object_or_404, redirect
from .models import FV, Product, Profile
from .forms import EditFV, SignUpForm
from django.template.defaulttags import register

# Create your views here.


def mainpage(request):
    return render(request, 'fakturownia/manage.html', {})

@login_required(login_url='login/')
def index(request):
    fv_s = FV.objects.order_by('-fv_date')
    prices = collections.defaultdict(int)

    for item in FV.objects.order_by('-fv_date'):
        prices[item.id] = item.products.all().aggregate(suma=Sum('price'))

    context = {
        'FV_s': fv_s,
        'prices': prices
    }
    return render(request, 'fakturownia/index.html', context)

@login_required(login_url='login/')
def detail(request, fv_id):
    fv = get_object_or_404(FV, pk=fv_id)
    suma = 0
    for item in fv.products.all():
        suma += item.price
    context = {
        'fv': fv,
        'suma': suma,
        'suma_netto': (suma - (suma * 0.23)),
        'suma_vat': suma * 0.23,
        'profile': User.objects.get(pk=request.user.id)
    }
    return render(request, 'fakturownia/show.html', context)

@login_required(login_url='login/')
def edit(request, fv_id):
    entry = get_object_or_404(FV, pk=fv_id)
    if request.method == "POST":
        form = EditFV(request.POST, instance=entry)
        if form.is_valid():
            inst = form.save(commit=False)

            products_id = request.POST['products_id']
            products_id = products_id.split(', ')
            inst.products.clear()
            for item in products_id:
                if item:
                    inst.products.add(Product.objects.filter(pk=item).get())

            inst.save()
            return redirect('detail', int(fv_id))
    else:
        form = EditFV(instance=entry)
        curr = ""
        for item in entry.products.all():
            curr += str(item.id)
            curr += ", "
        context = {'form': form, 'fv_id': int(fv_id), 'fv': entry, 'curr': curr}
        return render(request, 'fakturownia/edit.html', context)


@login_required(redirect_field_name='login/')
def search(request):
    if request.method == 'GET':
        prod = Product.objects.filter(name__icontains=request.GET['q'])
        rdy_html = ""
        for item in prod:
            rdy_html += '<p onClick="chooseThis(this,' + str(item.id) + ')" value=' + str(item.id) + '>'\
                        + item.name + " | " + str(item.price) + "</p><br />"
        if rdy_html == "":
            rdy_html += "Nic nie znaleziono"
    return HttpResponse(rdy_html)

@login_required(redirect_field_name='login/')
def delete(request, fv_id):
    FV.objects.filter(pk=fv_id).delete()
    return redirect('showall')

@login_required(redirect_field_name='login/')
def new(request):
    if request.method == "POST":
        form = EditFV(request.POST)
        if form.is_valid():
            entry = form.save(commit=True)
            products_id = request.POST['products_id']
            products_id = products_id.split(', ')
            for item in products_id:
                if item:
                    entry.products.add(Product.objects.filter(pk=item).get())

            entry.save()
            return redirect('detail', int(entry.id))
    else:
        form = EditFV()
    return render(request, 'fakturownia/new.html', {'form': form})

@login_required(redirect_field_name='login/')
def signup(request):
    print(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['reg_agree'] == u'on':
                print('reg_agreed')
                user = form.save(commit=True)
                user_id = User.objects.get(username=form.cleaned_data['username'])
                profile = Profile.objects.get_or_create(user=user_id,
                                                        seller_data=request.POST['seller_data'],
                                                        address=request.POST['address'],
                                                        nip=request.POST['nip'],
                                                        phonenumber=request.POST['phonenumber']
                                                        )
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('showall')
            else:
                print('reg_not_agreed')
                messages.warning(request, 'Zgoda jest wymagana')
                form = SignUpForm(request.POST)
                return render(request, 'registration/signup.html', {'form': form})
    else:
        messages.warning(request, 'Wszystkie pola są wymagane!')
        print('clean_render')
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(redirect_field_name='login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)