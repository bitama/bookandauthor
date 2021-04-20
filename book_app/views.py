from django.shortcuts import render,redirect
from .models import Book,Author

def index(request):
    context={
        "books":Book.objects.all()
    }
    return render(request,"index.html" ,context)

def book_create(request):
    Book.objects.create(
        title=request.POST["title"],
        description=request.POST["description"],
    )
    return redirect("/")

def author_views(request):
    context={
        "authors":Author.objects.all()
    }
    return render(request,"author.html",context)




def author_create(request):
    Author.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        notes = request.POST["notes"]
    )
    return redirect("/authors/view")

def book_view(request,book_id):
    context={
        
        "books":Book.objects.get(id=book_id)
        
    }
    return render(request,"book.html",context)

def another_authors_view(request,author_id):
    context={
        
        "authors":Author.objects.get(id=author_id)
        
    }
    return render(request,"otherauthor.html",context)


    