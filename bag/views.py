from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view tthat renders the pag content page """

    return render(request, 'bag/bag.html')