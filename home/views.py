from django.shortcuts import render

# Create views here.

def index(request):
    """
    A view that displays an index page
    """
    return render(request, "index.html")