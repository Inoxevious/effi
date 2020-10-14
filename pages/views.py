from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'pages/home.html')

def guide(request):

    return render(request, 'pages/guide.html')

def contact(request):

    return render(request, 'pages/contact.html')

# def register(request):

#     return render(request, 'pages/register.html')

def listing(request):

    return render(request, 'pages/listing.html')

# def loginn(request):
#     data = 'hie'
#     context = {'data':data}

#     return render(request, 'pages/login.html', context)

def primary(request):

    return render(request, 'pages/primary.html')

def secondary(request):

    return render(request, 'pages/secondary.html')

    
def faq(request):

    return render(request, 'pages/faq.html')