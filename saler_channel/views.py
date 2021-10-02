from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from saler_channel.models import ProfileShop
from store.models import Product
from django.views.generic import CreateView, UpdateView
from .forms import UpdateInfoShopForm

class Home(LoginRequiredMixin, View):

    def get(self, request):
        profileShop, profileShopCreated = ProfileShop.objects.get_or_create(
            user = request.user)
        if profileShopCreated:
            print("dang taoooooooo")
            profileShop.name_store = request.user.first_name + ' ' + request.user.last_name
            profileShop.save()
        print(profileShop.name_store)
        context = {'profileShop': profileShop}
        return render(request, 'saler_channel/saler_home.html', context = context)

class AllProduct(View):
    def get(self, request):
        profileShop = ProfileShop.objects.get(user = request.user)
        items = Product.objects.filter(profile_shop = profileShop)
        print(items)
        context = {'items': items}
        return render(request, 'saler_channel/saler_all_product.html', context = context)

class CreateProductView(CreateView):

    #để load được file ảnh cần phải setting cho file static trong app/setting.py
    #và thêm enctype="multipart/form-data" cho form bên Template
    model = Product
    fields = ['name', 'category' ,'price', 'image', 'description', 'quantity']
    template_name = 'saler_channel/create_product.html'

    def form_valid(self, form):
        form.instance.profile_shop = ProfileShop.objects.get(user = self.request.user)
        return super().form_valid(form)

class ProfileShopView(View):
    def get(self, request):
        profileShop = ProfileShop.objects.get(user = request.user)
        print(profileShop)
        form = UpdateInfoShopForm(instance = profileShop)
        context = {'form': form}
        return render(request, 'saler_channel/saler_profile_shop.html', context = context)
    
    def post(self, request):
        profileShop = ProfileShop.objects.get(user = request.user)
        form = UpdateInfoShopForm(request.POST, request.FILES, instance = profileShop)
        if form.is_valid():
            print('valid')
            form.save()
        else:
            print('unvalid')
        return redirect('saler_all_product')

class UpdateProductView(UpdateView):
    model = Product
    fields = ['name', 'category', 'price', 'description', 'image', 'quantity']
    template_name = 'saler_channel/update_product.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
