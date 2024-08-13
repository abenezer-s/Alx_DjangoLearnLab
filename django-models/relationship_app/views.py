from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .models import Book
from .models import Library

# Create your views here.

def  list_books(request):
    qs = Book.objects.all()
    context = {
        'books' : qs
    }

    return render(request, 'relationship_app/list_books.html',context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('book-view')  # Redirect to a success page
        
    
    return render(request, "relationship_app/login.html")

class LibraryDetailView(DetailView):
    model =Library
    template_name = 'relationship_app/library_detail.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/registration.html'



class LibraryLogoutView(LogoutView):
    next_page = 'relationship_app/login'  

