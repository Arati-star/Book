from django.shortcuts import render
from .models import  Book
# Create your views here.
def index(request):
    error = ""
    if request.method == 'POST':
        b = request.POST['bname']
        a = request.POST['aname']
        g = request.POST['gen']
        l = request.POST['lan']

        try:

            Book.objects.create(  Book_name=b, Author=a, Genre=g, Language=l)
            error = "No"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'intern/index.html', d)

    return render(request,'intern/index.html')
def book(request):
    book=Book.objects.all()
    d={'book':book}

    return render(request,'intern/book.html',d)
