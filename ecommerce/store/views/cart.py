from django.shortcuts import render
from django.views import View
from store.models.products import Products


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')

        if not cart:
            products = []
        else:
            products = Products.get_products_by_id(list(cart.keys()))

        return render(request, 'cart.html', {
            'products': products
        })