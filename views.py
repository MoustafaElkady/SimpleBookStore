from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden

from django.views.generic import ListView,DetailView

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Book
import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
User = get_user_model()


class Index(ListView):
    model = Book
    paginate_by = 30
    template_name = 'SimpleBookStore/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.select_related(
            'author', 'category'
        )

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['segment_title'] = 'New Books'
        return context

class BookView(DetailView):
    model = Book
    template_name = 'SimpleBookStore/book.html'

def login_view(request):
    if request.method == "GET":
        return render(request, 'SimpleBookStore/login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid = True
        if not username or not password:
            valid = False
            messages.add_message(request, messages.INFO, "Username and password cannot be empty")
        user = User.objects.filter(username=username).first()
        if not user:
            valid = False
            messages.add_message(request, messages.INFO, "User does not exist")
        user = authenticate(username=username, password=password)
        if (user is not None) and valid:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('SimpleBookStore:index'))
            else:
                valid = False
                messages.add_message(request, messages.INFO, "User deactivated")
        else:
            valid = False
            messages.add_message(request, messages.INFO, "Incorrect password")
        if not valid:
            return HttpResponseRedirect(reverse("SimpleBookStore:login"))


def register(request):
    if request.method == "GET":
        return render(request, 'SimpleBookStore/register.html')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        retype_password = request.POST.get("retype_password")
        valid = True
        if User.objects.filter(username=username).exists():
            valid = False
            messages.add_message(request, messages.INFO, "User already exists")
        if password != retype_password:
            valid = False
            messages.add_message(request, messages.INFO, "Password does not match")
        if not EMAIL_REGEX.match(email):
            valid = False
            messages.add_message(request, messages.INFO, "Invalid Email")
        if not valid:
            return HttpResponseRedirect(reverse("SimpleBookStore:register"))
        else:
            User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user = authenticate(
                username=username,
                password=password
            )
            login(request, user)
            return HttpResponseRedirect(reverse("SimpleBookStore:index"))


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("SimpleBookStore:index"))
