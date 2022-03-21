from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
# Create your views here.
from .forms import  FtyTableForm, ProductForm, RegistrationForm, OrderForm
from .decorators import unauthenticated_user

@login_required(login_url="login")
def home(request):
    orders = Order.objects.all()
    # customers = Customer.objects.all()

    # total_orders = orders.count()
    # total_customers = customers.count()

    # total_iphone_sold = Order.objects.filter(product__name='Iphone').count()

    # total_sales = Order.objects.aggregate(Sum('product__price'))['product__price__sum']

    context = {
        'total_orders': 5,
        'total_customers' : 10,
        'total_iphone_sold' : 13,
        'total_sales' : int(155),
        'orders' : orders,
    }
    return render(request, 'app/dashboard.html',context)
    # return HttpResponse('Hello World.')

@unauthenticated_user
def app_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect.')
    return render(request, 'app/authentication/login.html')

def app_logout(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for '+username+'.')
            return  redirect('login')
    
    context = {'form':form}
    return render(request, 'app/authentication/register.html', context)

def sample_page(request):
    orders = Order.objects.all()
    # orders = Order.objects.filter(status="Pending")
    context = {
        'orders' : orders,
    }
    return render(request, 'app/sample_page.html',context)

def order_details(request):
    # orderDetails = OrderDetail.objects.all()[:50]
    # orders = Order.objects.filter(status="Pending")
    # import pdb
    # pdb.set_trace()
    # context = {
    #     'orderDetails' : orderDetails,
    # }
    return render(request, 'app/order_details.html')

# def updateOrder(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)
#     print('ORDER:', order)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/sample_page')

#     context = {'form':form}
#     return render(request, 'app/order_form.html', context)



def show_order(request):
    return render(request, 'app/content/order/show_order.html')


def update_order(request, pk):
    order = Order.objects.get(order_pk=pk)
    form = OrderForm(instance=order)
    print('hello')
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            print('I"m in')
            form.save()
            return redirect('/order')

    context = {'form':form}
    return render(request, 'app/content/order/update_order.html', context)

def show_product(request):
    return render(request, 'app/content/product/show_product.html')

def update_product(request, pk):
    product = Product.objects.get(product_pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product')

    context = {'form':form}
    return render(request, 'app/content/product/update_product.html', context)

def create_fty_table(request):
    form = FtyTableForm()
    if request.method == 'POST':
        form = FtyTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/factory_table')
    
    context = {'form':form}
    return render(request, 'app/content/factory_table/create_factory_table.html',context)

def show_fty_table(request):
    return render(request, 'app/content/factory_table/show_factory_table.html')

# Rest Framework Views

from .serializer import *
from rest_framework import viewsets

from rest_framework import generics
from rest_framework.response import Response
from rest_framework_datatables import pagination as dt_pagination


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all().order_by('order_detail_pk')
    serializer_class = OrderDetailSerializer
    pagination_class = dt_pagination.DatatablesLimitOffsetPagination
    http_method_names = ['get', 'head']
    # class Meta:
    #     datatables_extra_json = ('get_options', )

# class OrderDetailListView(generics.ListAPIView):
#     queryset = OrderDetail.objects.all().order_by('order_detail_pk')
#     serializer_class = OrderDetailSerializer
#     pagination_class = dt_pagination.DatatablesLimitOffsetPagination

#     def post(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class FtyTableViewSet(viewsets.ModelViewSet):
    queryset = FtyTable.objects.all()
    serializer_class = FtyTableSerializer
    pagination_class = dt_pagination.DatatablesLimitOffsetPagination
    http_method_names = ['get', 'head']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = dt_pagination.DatatablesLimitOffsetPagination
    http_method_names = ['get', 'head']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = dt_pagination.DatatablesLimitOffsetPagination
    http_method_names = ['get', 'head']