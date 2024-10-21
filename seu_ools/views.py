from django.shortcuts import render
from study_planner.models import UserProfile

def home(request):
    # Check if the user is authenticated and get the user's profile
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None
    else:
        user_profile = None

    context = {
        'user_profile': user_profile
    }

    return render(request, 'home.html', context)
