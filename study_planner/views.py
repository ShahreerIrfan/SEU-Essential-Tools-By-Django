from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, UserProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.first_name = user_form.cleaned_data.get('first_name')
            user.last_name = user_form.cleaned_data.get('last_name')
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('profile')  
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'study_planner/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile or home page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'study_planner/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  #


@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'study_planner/profile_view.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  
    else:
        user_form = UserRegistrationForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'study_planner/edit_profile.html', context)
