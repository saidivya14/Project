from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import User,Profile

def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__ 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'Welcome {username} !!')
            return redirect('classroom:home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username).first()
            Profile.objects.create(user=user)
            email = form.cleaned_data.get('email')
            d = {'username': username}
            subject, from_email, to = 'Welcome', 'EngageProgram14@gmail.com', email
            content = 'Thanks {0} for registering'.format(username)
            msg = EmailMultiAlternatives(subject, content, from_email, [to])
            msg.send()
            messages.success(request, f'Account Created Successfully for {username}')
            return redirect('users:login')
        else:
            messages.success(request, f'Error Setting up the account')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(data=request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save(commit=False)
            profile = request.user.profile
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            messages.success(request, f"Profile Updated !")
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/profile.html', context)
