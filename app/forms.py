from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         widgets = {
#                         'status': forms.TextInput(attrs={'readonly': True}),
#                         # 'note': forms.TextInput(attrs={'readonly': True}),
#                         }

# class OrderFormBase(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         # widgets = {
#         #                 'status': forms.TextInput(attrs={'readonly': True}),
#         #                 # 'note': forms.TextInput(attrs={'readonly': True}),
#         #                 }
# class OrderForm(OrderFormBase):
#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)
#         print(self.fields)
#         self.fields['status'].widget = forms.TextInput(attrs={'readonly': True})


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('order_pk',)
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        read_only_fields = ['ic', 'delivery', 'date_placed', 'destination', 
                            'consol_num', 'fob', 'due', 'account', 'asn_no',
                            'status', 'units', 'total_cartons_in_order',
                             'delivery_ean', 'container_number', 'arrival_date',]

        date_input_fields = [ 'date_booked','crd', 'forwarder_given_etd', 'forwarder_given_eta', 'handover_date']
        for field in iter(self.fields):
            if field in read_only_fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'readonly' : True,
                })
            elif field in date_input_fields:
                self.fields[field].widget = forms.DateInput(attrs={'type': 'date','class': 'form-control'})
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : field.replace('_',' ').title(),
                })

        # for col in read_only_fields:
        #     self.fields[col].widget = forms.TextInput(attrs={'readonly': True})



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('product_pk',)
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        print(self.fields)
        read_only_fields = [
                                'dept', 'styl', 'colour', 'size', 'description', 'date_created', 'user_verified',
                                'chkdigit', 'supplier_code', 'account', 'tla_fty_code', 'cust_fty_code',
                                'barcode', 'trading_code'
                            ]

        date_input_fields = ['photo_sample_date']
        for field in iter(self.fields):
            if field in read_only_fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'readonly' : True,
                })
            elif field in date_input_fields:
                self.fields[field].widget = forms.DateInput(attrs={'type': 'date','class': 'form-control'})
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : field.replace('_',' ').title(),
                })

class FtyTableForm(ModelForm):
    class Meta:
        model = FtyTable
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(FtyTableForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder' : field.replace('_',' ').title(),
            })

        self.fields['compliance_expiry'].widget = forms.DateInput(attrs={'type': 'date','class': 'form-control'})


# class ICDeliverySelectionForm(forms.ModelForm):

#     class Meta:
#         model = OrderDetail
#         fields = ['ic','delivery']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['ic'].queryset = OrderDetail.objects.none()
#         self.fields['delivery'].queryset = OrderDetail.objects.none()

