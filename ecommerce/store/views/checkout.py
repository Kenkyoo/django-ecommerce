from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from store.models.products import Products
from store.models.orders import Order


class CheckOut(View):

    def get(self, request):
        cart = request.session.get('cart', {})

        if not cart:
            return redirect('cart')

        products = []
        total = 0
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

        return render(request, 'checkout.html', {
            'products': products,
            'total': total,
        })

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart', {})

        product_list = Products.get_products_by_id(list(cart.keys()))
        for product in product_list:
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id), 1),
            )
            order.save()

        request.session['cart'] = {}
        return redirect('orders')