from django.views.generic import DetailView, TemplateView, ListView, FormView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from orders.models import Order, OrderItem
from wishlist.models import WishList
from random import randint
from django import forms
from .forms import *


class PersonalInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard_personal_info.html'
    context_object_name = 'user'
    
    def post(self,reqeust, **kwargs):
        user = request.user
        context = {'user':user}
        return render(request, 'accounts/personal_info.html', context)

class PersonalInfoEditView(UpdateView):
    template_name = 'accounts/dashboard_personal_info_edit.html'
    model = User
    fields = ['image','email','nickname', 'first_name', 'last_name', 'bio']
    success_url = reverse_lazy('accounts:user_personal_info')

    def form_valid(self, form):
        data = self.request.POST
        image_data = self.request.FILES
        if image_data:
            image = image_data['image']
        email = data.get('email')
        nickname = data.get('nickname')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        bio = data.get('bio')
        messages.success(self.request, "personal info updated", 'success')
        return super().form_valid(form)


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'accounts/dashboard_wishlist.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        user = self.request.user
        return WishList.objects.filter(user=user)


class ProductsPurchasedView(LoginRequiredMixin, ListView):
    template_name = 'accounts/dashboard_product_purchased.html'
    context_object_name = 'products_purchased'

    def get_queryset(self):
        user = self.request.user
        products_purchased = []
        order = Order.objects.filter(user=user, paid=True)
        for item in order:
            orderitem = OrderItem.objects.filter(order=item)
            for item in orderitem:
                products_purchased.append(item.product)
        return products_purchased

# class UserLoginView(TemplateView):
#     template_name = 'accounts/login_choice.html'

def UserLoginView(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login_choice.html')
    else:
        return redirect('accounts:user_personal_info')


class ApiView(TemplateView):
    template_name = 'accounts/API_info.html'


def user_login_pw(request):
    if request.method == 'POST':
        form = LoginWithPwForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'you loggined successfully', 'success')
                return redirect('accounts:user_personal_info')
            else:
                messages.error(
                    request, 'username or password is incorrect', 'warning')
    else:
        form = LoginWithPwForm()
    context = {'loginform': form}
    return render(request, 'accounts/login_with_password.html', context)


def user_login_code(request):
    if request.method == 'POST':
        form = LoginWithCodeForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            code = randint(1000, 9999)
            request.session['verify_code'] = code
            request.session['phone'] = phone
            print("="*30)
            print(f'verify code is : {code}')
            print("="*30)
            return redirect('accounts:login_verify_code')
    else:
        form = LoginWithCodeForm()

    context = {
        'loginform': form,
        }
    return render(request, 'accounts/login_with_code.html', context)


def login_verify_code(request):
    code = request.session['verify_code']
    phone = request.session['phone']
    if request.method == 'POST':
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            if int(code) == int(form.cleaned_data['code']):
                user = get_object_or_404(get_user_model(), phone=phone)
                if user is not None:
                    login(request, user)
                messages.success(request, 'you loggined successfully', 'success')
                return redirect('accounts:user_personal_info')
            else:
                messages.error(request, 'your code is wrong', 'warning')
    else:
        form = VerifyCodeForm()

    context = {'verifycode': form}
    return render(request, 'accounts/login_with_code_verify.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # create account
            user = get_user_model().objects.create_user(cd['phone'], cd['nickname'], cd['phone'])
            if user is not None:
                login(request, user)
            messages.success(request, 'you successfully registered and now you can verify you account or enter your account without verifing', 'success')
            # verify account section 
            phone = cd['phone']
            code = randint(1000, 9999)
            request.session['verify_code'] = code
            request.session['phone'] = phone
            print("="*30)
            print(f'verify code is : {code}')
            print("="*30)
            return redirect('accounts:register_verify_phone')
    else:
        form = UserCreationForm()
    context = {
        'registerform': form
    }
    return render(request, 'accounts/register.html', context)


def register_verify_phone(request):
    code = request.session['verify_code']
    phone = request.session['phone']
    if request.method == 'POST':
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            if int(code) == int(form.cleaned_data['code']):
                user = get_object_or_404(User, phone=phone)
                user.is_verify = True
                user.save()
                if user is not None:
                    login(request, user)
                messages.success(request, 'your account verfied successfully and you logged in', 'success')
                return redirect('accounts:user_personal_info')
    else:
        form = VerifyCodeForm()
    context = {
        'verify_registerform': form
    }
    return render(request, 'accounts/register_verify.html', context)


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('shop:home')
