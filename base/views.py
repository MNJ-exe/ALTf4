from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'base/about.html')
def contact_view(request):
    return render(request, 'base/contact.html')