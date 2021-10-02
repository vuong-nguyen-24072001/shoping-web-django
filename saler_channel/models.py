from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class ProfileShop(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    avatar = models.ImageField(default = 'default.jpg', null = True, blank = True)
    name_store = models.CharField(max_length = 50, default = 'YourNameShop...' ,null = True, blank = True)
    description = models.CharField(max_length = 250, null = True, blank = True)
    phone_number = models.CharField(max_length = 15, null = True, blank = True)

    def __str__(self):
        return self.name_store

    def save(self, **kwargs):
        img = Image.open(self.avatar)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300,300))
            img.save(self.avatar.path)
        super().save()

    
