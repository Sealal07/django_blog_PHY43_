from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateFrom, ProfileUpdateFrom

@login_required
def profile_view(request):

    if request.method == 'POST':
        u_form = UserUpdateFrom(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile') #обновление страницы
    else:
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'profiles/profile.html', context)



# Create your views here.
