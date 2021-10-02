from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from saler_channel.models import ProfileShop
from django.urls import reverse
from PIL import Image

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, null = True) 
    phone_number = models.CharField(default = '', max_length = 20)

    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    image = models.ImageField(default = 'placeholder.png', upload_to = 'product_images')

    def __str__(self):
        return self.name

class Product(models.Model):
    profile_shop = models.ForeignKey(ProfileShop, on_delete = models.SET_NULL, null = True, blank = True)
    category = models.ForeignKey(Categorie, on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    name = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null = True, blank = True)
    image = models.ImageField(default = 'placeholder.png', upload_to = 'category_images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('saler_all_product')

    def save(self):
        super().save()
        img = Image.open(self.image)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300,300))
            img.save(self.image.path)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = True)
    transaction_id = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return str(self.customer)

    @property
    def get_cart_total(self):
        orderitems = self.order_items_related.all()
        total = sum([item.get_total for item in orderitems])
        return round(total, 2)

    @property
    def get_cart_item(self):
        orderitems = self.order_items_related.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, related_name="order_items_related",  on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    #property định danh 1 getter get_total
    #nếu k có property, nếu trỏ tới method này từ OrderItem thì kết quả trả về chỉ là 1 method
    #nếu có property get_total là 1 getter, hay có thể coi property là biến một method thành 1 attribute
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return round(total, 2)

class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True)   
    city = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 200, null = True)
    zipcode = models.CharField(max_length = 200, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.address
