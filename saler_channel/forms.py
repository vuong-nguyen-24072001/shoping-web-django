from django import forms
from saler_channel.models import ProfileShop
from store.models import Product

class UpdateInfoShopForm(forms.ModelForm):

    class Meta:
        model = ProfileShop
        fields = ['avatar', 'name_store', 'description', 'phone_number']


