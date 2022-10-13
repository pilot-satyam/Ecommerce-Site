from audioop import add
from operator import eq
import re
from django.shortcuts import render
from .models import Order, Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    product_objects = Products.objects.all()

    #search code

    item_name = request.GET.get('item_name') #getting the item name from input field in html file for searching
    if item_name !='' and item_name is not None:
        product_objects = product_objects.filter(title__icontains = item_name)
        
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page') #now passing this page to paginator to get that page
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects':product_objects})

#we require id for the details as we will click on particular product and then its details dhould be displayed
def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"") #in this bracket first field is for the name of the element which we have included already in checkout page, second field is for default value
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zip=zip,total=total) #above extracted items are saved in this object
        order.save()
    return render(request,'shop/checkout.html')
