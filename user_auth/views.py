from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def register(request):
    """
    Handles new user registration.

    If the request method is POST, it processes the registration form,
    validates it, and saves the new user. If successful, it redirects 
    the user to the login page with a success message. If the metho is 
    GET, it displays an empty regisstration form.

    Arguments:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the registration template for GET 
        requests or redirects to the login page after successful
        registration.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You "
                             "can now login")
            return redirect('login')
        else:
            # Render form with errors.
            return render(request, 'registration/register.html', {'form': form
                                                                  })
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    """
    Logs in user for 'polls' app.

    Retrieves user login and renders it using 
    'authentication/login.html' template.
    """
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    """
    Authenticates user login.

    Retrieves user in 'User' table. If user does not exist, 
    returns "None" and re-renders "authentication/login.html", if does
    exist renders 'authentication/user.html' template.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
            )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
            )


def show_user(request):
    """
    Display user login.

    Retrieves user login and renders it using 'authentication/user.html'
    template.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
        })
