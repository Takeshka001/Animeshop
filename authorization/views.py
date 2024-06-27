from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm, CustomerAuthenticationForm, CustomerUserEditForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request): 
    context = {
        'user': request.user, 
    }
    return render(request, 'home.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomerUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('auth:profile')
    else:
        form = CustomerUserEditForm(instance=request.user)
    return render(request, 'authorization/profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:login')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'authorization/register.html', {'form': form})


class CustomerLoginView(LoginView):
    authentication_form = CustomerAuthenticationForm
    template_name = 'login.html'
    redirect_field_name = 'home'
    redirect_authenticated_user = True

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'authorization/home.html')

