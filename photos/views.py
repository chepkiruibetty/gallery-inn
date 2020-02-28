from django.shortcuts import render
from django.views.generic import ListView

from .models import Images,Category,Location

# Create your views here.
def home(request):
    images= Images.objects.all()
    return render(request, "home.html", {"images":images})

def search_image(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    if 'images' in request.GET and request.GET['image']:
        search_item =request.GET.get('image')
        found_results=Image.get_image_by_cate(search_item)
        message=f"{search_item}"
        print(found_results)
        
        return render(request, 'search.html',
                    {'found_results': found_results, 'message': message, 'categories': categories,
                    "locations": locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html', {"message": message})
    
    
def categories(request):
    categories = Image.get_all_images()
    return render(request, 'categories.html', {"categories": categories})


def search_image_by_category(request,locs):
    my_images = Image.get_image_by_location(locs)
    print(my_images)
    return render(request, 'location.html', {"my_images": my_images})


def single_image(request,image_id):
    image=Image.objects.get(id = image_id)
    return render(request, 'image.html',{"image":image})


