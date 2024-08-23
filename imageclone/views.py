from django.shortcuts import render,redirect 
from django.db.models import Q 
from django.http import HttpResponse  
from imageshop.models import * 


# Create your views here.
def home(request): 
    images=Image.objects.all()  
    cats=Category.objects.all() 
    data={'images':images,'cats':cats}  
    return render(request,"home.html",data) 

def show_category_page(request,cid):     
    cats=Category.objects.all()  
    catg=Category.objects.get(pk=cid)   
    images=Image.objects.filter(cat=catg)
    data={'images':images,'cats':cats}  
    return render(request,"home.html",data)    

def search(request):
    query = request.GET.get('query') 

    if query:
        # Check if query matches a category title
        category = Category.objects.filter(title__iexact=query).first()
        if category:
            return redirect('show_category_page', cid=category.pk)
        
        # Check if query matches an image title
        image = Image.objects.filter(title__iexact=query).first()
        if image:
            # Here you would redirect to an image-specific page if such exists
            # For example: return redirect('show_image_page', image_id=image.pk)
            # For now, we'll render a search page with just that image
            return render(request, 'search.html', {'images': [image]})
        
        # If no exact match, fall back to containing matches
        images = Image.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
        categories = Category.objects.filter(title__icontains=query)
        
        # Display the search results page
        return render(request, 'search.html', {'images': images, 'categories': categories}) 
    
    return redirect('home') 
