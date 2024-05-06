from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	#quantities = cart.get_quants
	#totals = cart.cart_total()
	return render(request, "cart_summary.html", {"cart_products":cart_products})



def cart_add(request):
	 # Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product)
		#get quantity
		cart_quantity = cart.__len__()
		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty':cart_quantity })
		return response

def cart_delete(request):
	pass


def cart_update(request):
	pass
