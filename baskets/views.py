from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from mainapp.models import Product
from baskets.models import Basket


# Create your views here.

@login_required
def basket_add(request, product_id):
    prod = Product.objects.get(id=product_id)
    # =============================================
    baskets = Basket.objects.filter(user=request.user, products=prod)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=prod, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def basket_remove(request, b_id):
    Basket.objects.get(id=b_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
