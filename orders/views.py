from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.sessions import Cart
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from django.contrib import messages


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/checkout.html', {'order': order})


@login_required
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(
            order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    return redirect('orders:detail', order.id)


MERCHANT = 'b9602f98-9375-11e6-82ab-000c295eb8fc'
client = Client('http://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required  # Optional
CallbackURL = 'http://localhost:8000/orders/verify/' # Important: need to edit for realy server.

@login_required
def send_request(request,order_id, price):
    global amount, orderid
    amount = price
    orderid = order_id
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, request.user.phone, CallbackURL)
    if result.Status == 100:
        return redirect('http://zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

@login_required
def verify(request):
    cart = Cart(request)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order = Order.objects.get(id=orderid)
            order.paid = True
            cart.clear()
            order.save()
            messages.success(request, 'Transaction was successful', 'success')
            return redirect('shop:home')
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')