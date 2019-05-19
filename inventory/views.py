from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm
from .forms import OutgoingForm
from .models import outgoing_supply
from .forms import IncomingForm
from .models import incoming
from .forms import historyForm
from django.db.models import Q
#from dal.autocomplete import Select2ListView
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/index.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/detail.html', {'product': product})


def outgoing(request):
    #form=OutgoingForm()
    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        quantity = int(request.POST['quantity'])
        #print(product_id, "--", quantity)
        # Query the database
        product_ids_list=Product.objects.all().order_by('id')
        #for i in product_ids_list:

        #    print(i.id)

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
            #return redirect('index')
        return render(request, 'inventory/outgoing.html', {'id':product_ids_list})
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
                    items.quantity = items.quantity + int(request.POST['quantity'])
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


def history(request):
    if request.method == 'POST':
        search_content=request.POST['search_content']
        start=request.POST['start']
        end=request.POST['end']
        option=request.POST['option']
        ## If option selected Incoming
        if option == "Incoming":
            
            #print(request.POST)
            
            if search_content and start and end:

                end=end + " 23:59:59"
                condition=((Q(name__icontains=str(search_content)) | Q(cetagory__contains=str(search_content)) | Q(supplier__contains=str(search_content)) | Q(description__contains=str(search_content))) & Q(date__range=[start, end]))
                lookups= incoming.objects.filter(condition)
                    #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/incoming_history.html', context)
            elif search_content and not start and not end:
                condition=((Q(name__icontains=str(search_content)) | Q(cetagory__contains=str(search_content)) | Q(supplier__contains=str(search_content)) | Q(description__contains=str(search_content))))
                lookups= incoming.objects.filter(condition)
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/incoming_history.html', context)
            elif not search_content and start and end:
                end=end + " 23:59:59"
                condition=(Q(date__range=[start, end]))
                lookups= incoming.objects.filter(condition)
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/incoming_history.html', context)
            else:
                lookups= incoming.objects.all()
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/incoming_history.html', context)
        ## If option selected Outgoing
        elif option == "Outgoing":
            if search_content and start and end:
                print(request.POST)
                end=end + " 23:59:59"
                if search_content.isdigit():
                    condition=((Q(engg_name__icontains=str(search_content)) | Q(product_id__icontains=int(search_content))) & Q(date__range=[start, end]))
                else:
                    condition=((Q(engg_name__icontains=str(search_content))) & Q(date__range=[start, end]))
                lookups= outgoing_supply.objects.filter(condition)
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/outgoing_history.html', context)
            elif search_content and not start and not end:
                if search_content.isdigit():
                    condition=(Q(engg_name__icontains=str(search_content)) | Q(product_id__icontains=int(search_content)))
                else:
                    condition=(Q(engg_name__icontains=str(search_content)))
                lookups= outgoing_supply.objects.filter(condition)
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/outgoing_history.html', context)
            elif not search_content and start and end:
                end=end + " 23:59:59"
                condition=(Q(date__range=[start, end]))
                lookups= outgoing_supply.objects.filter(condition)
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/outgoing_history.html', context)
            else:
                lookups= outgoing_supply.objects.all()
                #print("lookups :", lookups)
                context={'lookups': lookups}
                return render(request, 'inventory/outgoing_history.html', context)

    else:
        # A POST request: Handle Form Upload
        form = historyForm(request.POST) # Bind data from request.POST into a PostForm
        if form.is_valid():
            pass
            return redirect('index')
 
        return render(request, 'inventory/history.html', {'form': form})
