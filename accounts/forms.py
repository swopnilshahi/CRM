#using model forms
from django.forms import ModelForm
from . models import Order

# form class
class OrderForm(ModelForm):# we inherited from ModelForm
    class Meta:
        model = Order 
        fields = '__all__' #we want all field