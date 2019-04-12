from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm
from .forms import OutgoingForm
from .models import outgoing
from .forms import IncomingForm
from .models import incoming


#from dal.autocomplete import Select2ListView
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/index.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/detail.html', {'product': product})


def outgoing(request):
    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        quantity = int(request.POST['quantity'])
        #print(product_id, "--", quantity)
        # Query the database
        products = Product.objects.filter(id=product_id)
        for items in products:
            #print(items.id, items.quantity)
            
            if product_id == items.id and quantity <= items.quantity:
                #print("IN if block")
                # Updating the incoming object as product moved out
                items.quantity = items.quantity - quantity
                items.save()
                #print("Quantity : ", items.quantity)
                #print("Saved")
                # Saving the outgoing/moved product in database
                form = OutgoingForm(request.POST)
                #print("Saved Outgoing Form")
                if form.is_valid():
                    form.save()
                    return redirect('index')
            return redirect('index')
    else:
        form = OutgoingForm()
        return render(request, 'inventory/outgoing.html', {'form': form})

def addnew(request):
    if request.method == 'POST':
        name=request.POST['name']
        cetagory=request.POST['cetagory']
        supplier=request.POST['supplier']
        print(name, cetagory, supplier)
        products = Product.objects.filter(name=name)
        count= Product.objects.filter(name=name).count()
        print(count)
        if count > 0:
            for items in products:
                if name==items.name and cetagory==items.cetagory and supplier==items.supplier:
                    print("Items Saved")
                    items.save()
                    print("Items Saved")
        ##Insert the Incoming products to product table
        else:
            form = ProductForm(request.POST)
            form.save(commit=True)
        ##Insert the Incoming products to incoming table
        form=IncomingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('index')
                
    else:
        form = ProductForm()
        return render(request, 'inventory/new.html', {'form': form})

def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit.html', {'form': form})
