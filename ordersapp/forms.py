from django import forms

from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)

        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control'}),
            'created': forms.DateTimeInput(attrs={
                'class': 'form-control'}),
            'updated': forms.DateTimeInput(attrs={
                'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-control'}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ()

    def __int__(self, *args, **kwargs):
        super(OrderItemForm, self).__int__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.wiget.attrs['class'] = 'form-control'
