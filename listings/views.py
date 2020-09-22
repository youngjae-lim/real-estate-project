from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing


def index(request):
    # order listings by list_date and show listings with only is_published=True
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) 
    
    paginator = Paginator(listings, 6) # 3 listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
