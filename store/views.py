from typing import List
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.views.generic import DetailView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAllProductSerializer, GetAllCartItemSerializer

class Store(ListView):
    paginate_by = 12
    model = Product
    context_object_name = 'products'
    template_name = 'store/store.html'
    ordering = ['category']

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'categories': Categorie.objects.all(),
        })
        return context

class Cart(LoginRequiredMixin, View):
    
    def get(self, request):
        customer, created_new_customer = Customer.objects.get_or_create(user = request.user, name = request.user.first_name + request.user.last_name)
        order, created_new_order = Order.objects.get_or_create(customer = customer, complete = False)
        self.items = order.order_items_related.all()
        context = {'items': self.items, 'order': order}
        return render(request, 'store/cart.html', context)

class CheckOut(LoginRequiredMixin, View):
    def get(self, request):
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.order_items_related.all()
        context = {'items': items, 'order': order}
        return render(request, 'store/checkout.html', context)

class UpdateJson(LoginRequiredMixin, View):
    def get(self, request):
        return JsonResponse('Item was added', safe = False)

    def post(self, request):
        data = json.loads(request.body)
        productID = data['productID']
        action = data['action']
        print('productID:', productID, 'action:', action)

        customer = request.user.customer
        product = Product.objects.get(id = productID)
        order, created = Order.objects.get_or_create(customer = customer, complete = False)

        orderitem, created = OrderItem.objects.get_or_create(order = order, product = product)

        if action == 'add':
            orderitem.quantity = (orderitem.quantity + 1)
        elif action == 'remove':
            orderitem.quantity = (orderitem.quantity - 1)
        
        orderitem.save()
        
        if orderitem.quantity <= 0:
            orderitem.delete()

        return JsonResponse('Item was added', safe = False)

class ProductDetaiView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

class GetAllProductAPIView(APIView):

    def get(self, request):
        list_product = Product.objects.all()
        data_response = GetAllProductSerializer(list_product, many = True)
        return Response(data = data_response.data, status = status.HTTP_200_OK)

class GetAllCartItemAPIView(APIView):

    def get(self, request):
        list_cart_item = OrderItem.objects.all()
        data_response = GetAllCartItemSerializer(list_cart_item, many = True)
        return Response(data = data_response.data, status = status.HTTP_200_OK)

