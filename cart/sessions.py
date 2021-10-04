from shop.models import Product

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {} #create new session for cart if cart not exists
        self.cart = cart
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            if item['product'].discount:
                item['price'] = item['product'].price_after_set_discount()
            item['total_price'] = float(item['price']) * item['quantity']
            yield item

    def add_cart(self,product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            if product.discount:
                product.price = product.price_after_set_discount()
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()
    
    def remove_cart(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()