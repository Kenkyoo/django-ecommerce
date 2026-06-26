from django.shortcuts import render
from django.views import View
from store.models.products import Products

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        products = []
        total = 0

        if cart:
            product_list = Products.get_products_by_id(list(cart.keys()))
            for product in product_list:
                quantity = cart.get(str(product.id), 0)
                subtotal = product.price * quantity
                total += subtotal
                products.append({
                    'product': product,
                    'quantity': quantity,
                    'subtotal': subtotal,
                })

        return render(request, 'cart.html', {
            'products': products,
            'total': total,
        })